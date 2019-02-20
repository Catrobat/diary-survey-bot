"""
diary-survey-bot 2.0

Software-Design: Philipp Feldner
Documentation: https://github.com/Catrobat/diary-survey-bot

Telegram API:
https://github.com/python-telegram-bot/python-telegram-bot
"""

import sqlite3
import pickle
import shutil
import re

from datetime import datetime
from pytz import timezone
from pytz.exceptions import UnknownTimeZoneError

import random
import csv

from admin.settings import SCHEDULE_INTERVALS
from admin.settings import QUICK_TEST
from admin.settings import DEFAULT_TIMEZONE
from admin.debug import debug
from admin.survey_specific import survey_function

from telegram import Bot, Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Job, JobQueue
from telegram import TelegramError

from survey.data_set import DataSet
from survey.participant import Participant
from survey.keyboard_presets import CUSTOM_KEYBOARDS
from survey.keyboard_presets import TRANSLATE_EMOJI
import survey.keyboard_presets as kb_presets


# Calculates seconds until a certain hh:mm
# event. Used for the job_queue mainly.
# Timezones are already handled.
def calc_delta_t(time, days, zone=None):
    # If the admin setting QUICK_TEST the block scheduling ist 60s
    if QUICK_TEST is not False:
        return QUICK_TEST
    hh = time[:2]
    mm = time[3:]

    if zone is not None:
        try:
            current = datetime.now(timezone(zone))
        except UnknownTimeZoneError:
            current = datetime.now(timezone(DEFAULT_TIMEZONE))
    else:
        current = datetime.now()
    future = datetime(current.year, current.month, current.day, int(hh), int(mm), tzinfo=current.tzinfo)
    offset = future - current
    if offset.days == -1 and days > 0:
        days -= 1
    return offset.seconds + (days * 86400)


# Generates a random time offset
# for the next block that shall be scheduled.
# The intervals are defined in admin/settings.py
def calc_block_time(time_t):
    try:
        interval = SCHEDULE_INTERVALS[time_t]
    except KeyError:
        debug("BLOCK", "Error undefined schedule interval", log=True)
        return "00:00"

    if isinstance(interval, str):
        return interval

    hh_start = int(interval[0][:2])
    hh_end = int(interval[1][:2])
    mm_begin = int(interval[0][3:])
    mm_end = int(interval[1][3:])

    if hh_start < hh_end:
        value_hh = random.randint(hh_start, hh_end)
        if value_hh == hh_start:
            value_mm = random.randint(mm_begin + 10, 59)
        elif value_hh == hh_end:
            value_mm = random.randint(0, mm_end)
        else:
            value_mm = random.randint(0, 59)

    elif hh_start == hh_end:
        value_hh = hh_start
        value_mm = random.randint(mm_begin + 10, mm_end - 10)
    else:
        value_hh = random.choice[random.randint(hh_start, 23), random.randint(0, hh_end)]
        if value_hh == hh_start:
            value_mm = random.randint(mm_begin + 10, 59)
        elif value_hh == hh_end:
            value_mm = random.randint(0, mm_end)
        else:
            value_mm = random.randint(0, 59)

    return str(value_hh).zfill(2) + ':' + str(value_mm).zfill(2)


# This function does the main handling of
# user questions and answers.
# This is function is registered in the Dispatcher.
def question_handler(bot: Bot, update: Update, user_map: DataSet, job_queue: JobQueue):
    try:
        # Get the user from the dict and its question_set (by language)
        user = user_map.participants[update.message.chat_id]  # type: Participant

        # Case for very first question.
        if user.question_ == -1:
            user.set_active(True)
            user.set_language(update.message.text)
            user.set_block(0)
            q_set = user_map.return_question_set_by_language(user.language_)
            user.q_set_ = q_set
            current_day = q_set[0]["day"]
            user.set_day(current_day)
            user.set_block(0)
        elif user.q_idle_:
            q_set = user.q_set_
            # Get the matching question for the users answer.

            pointer = user.pointer_
            d_prev = q_set[pointer]

            b_prev = d_prev["blocks"][user.block_]
            q_prev = b_prev["questions"][user.question_]

            if not valid_answer(q_prev, update.message.text, user):
                user.set_q_idle(True)
                return
            # Storing the answer and moving on the next question
            store_answer(user, update.message.text, q_prev, job_queue)
            user.set_q_idle(False)
        else:
            # User has send something without being asked a question.
            return
    except KeyError as error:
        print(error)
        return

    if not user.active_:
        return

    message, question = find_next_question(user)
    if question is not None:
        message = question["text"]
        q_keyboard = get_keyboard(question["choice"], user)
        try:
            bot.send_message(chat_id=user.chat_id_, text=message, reply_markup=q_keyboard)
            debug(flag="MSG", text=str(user.chat_id_) + ": " + message + "\n")
        except TelegramError as error:
            if error.message == 'Unauthorized':
                user.pause()

        user.set_q_idle(True)
    elif user.auto_queue_ is False:
        user.block_complete_ = True
        next_day = user.set_next_block()
        if next_day is None:
            finished(user, job_queue)
            return
        element = user.next_block[2]
        day_offset = next_day - user.day_
        time_t = calc_block_time(element["time"])
        due = calc_delta_t(time_t, day_offset, user.timezone_)

        debug('QUEUE', 'next block in ' + str(due) + ' seconds. User: ' + str(user.chat_id_), log=True)
        new_job = Job(queue_next, due, repeat=False, context=[user, job_queue])
        user.job_ = new_job
        job_queue._put(new_job)


# This function is getting used to generate
# the CSV files and store values.
# Also the conditions, DB values get set here.
def store_answer(user, message, question, job_queue):
    commands = question['commands']
    if message != '':
        for element in commands:
            # -- DB TRIGGER for storing important user data -- #
            if element[0] == "TIMEZONE":
                user.set_timezone(message)
            elif element[0] == "COUNTRY":
                user.set_country(message)
            elif element[0] == "GENDER":
                user.set_gender(message)
            elif element[0] == "AGE":
                user.set_age(message)
            elif element[0] == "Q_ON":
                user.auto_queue_ = True
                next_day = user.set_next_block()
                if next_day is None:
                    finished(user, job_queue)
                    continue
                element = user.next_block[2]
                day_offset = next_day - user.day_
                time_t = calc_block_time(element["time"])
                due = calc_delta_t(time_t, day_offset, user.timezone_)

                debug('QUEUE', 'next block in ' + str(due) + ' seconds. User: ' + str(user.chat_id_), log=True)
                new_job = Job(queue_next, due, repeat=False, context=[user, job_queue])
                user.job_ = new_job
                job_queue._put(new_job)
            elif element[0] == "DATA":
                if element[2] == "ADD":
                    if element[1] not in user.data_set_:
                        user.data_set_[element[1]] = []
                    user.data_set_[element[1]] += [int(message)]
                    user.set_data_set(user.data_set_)
                elif element[2] == "CLEAR" or element[2] == "CLR":
                    if element[1] in user.data_set_:
                        del user.data_set_[element[1]]
                        user.set_data_set(user.data_set_)

        condition = question["condition"]
        for element in condition:
            if message == element[0]:
                user.add_conditions(element[1])

        if message in TRANSLATE_EMOJI:
            message = TRANSLATE_EMOJI[message]

    if message == '':
        timestamp = ''
    elif user.timezone_ == '':
        timestamp = datetime.now().isoformat()
    else:
        try:
            timestamp = datetime.now(timezone(user.timezone_)).isoformat()
        except UnknownTimeZoneError:
            timestamp = 'Invalid Timezone'

    q_var = question['variable']
    q_text = question['text']
    q_text = q_text.replace('\n', ' ')
    q_text = q_text.replace(';', ',')
    message = message.replace('\n', ' ')
    message = message.replace(';', ',')

    with open('survey/data_incomplete/' + str(user.chat_id_) + '.csv', 'a+', newline='') as user_file:
        columns = [str(user.chat_id_), user.language_, user.gender_, user.age_, user.country_, user.timezone_,
                   user.day_, user.block_, user.question_, timestamp, q_text, message, q_var]
        writer = csv.writer(user_file, delimiter=';')
        writer.writerow(columns)

    return


# This function is called by the job_queue
# and starts all the blocks after the set time.
# It also calls itself recursively to assure progressing.
def queue_next(bot: Bot, job: Job):
    user = job.context[0]  # type: Participant
    job_queue = job.context[1]
    if not user.active_:
        return
    user.block_complete_ = False
    user.job_ = None

    # Stores all unanswered questions to csv
    prev = user.q_set_[user.pointer_]["blocks"][user.block_]["questions"]
    for i in range(user.question_, len(prev)):
        user.increase_question()
        q_prev = prev[i]
        store_answer(user, '', q_prev, job_queue)

    user.set_question(0)
    user.set_pointer(user.next_block[0])
    user.set_block(user.next_block[1])
    element = user.next_block[2]
    user.set_day(user.q_set_[user.pointer_]['day'])

    if ['MANDATORY'] in element['settings']:
        user.auto_queue_ = False
    else:
        user.auto_queue_ = True

    # Check if the user is currently active
    if not user.active_:
        return

    try:
        # Find next question that the user should get.
        while not user.check_requirements(element["questions"][user.question_]):
            store_answer(user, '', element["questions"][user.question_], None)
            user.increase_question()
    except IndexError:
        # User did not fulfill any questions for the day so we reschedule.
        # Set the new day.
        next_day = user.set_next_block()
        if user.next_block is None:
            return finished(user, job_queue)

        element = user.next_block[2]
        day_offset = next_day - user.day_
        time_t = calc_block_time(element["time"])
        due = calc_delta_t(time_t, day_offset, user.timezone_)

        # Add new job and to queue. The function basically calls itself recursively after x seconds.
        debug('QUEUE', 'next block in ' + str(due) + ' seconds. User: ' + str(user.chat_id_), log=True)
        new_job = Job(queue_next, due, repeat=False, context=[user, job_queue])
        user.job_ = new_job
        job_queue._put(new_job)
        return

    # Sending the question
    question = element["questions"][user.question_]
    message = parse_question(user, element["questions"][user.question_])
    q_keyboard = get_keyboard(question["choice"], user)
    try:
        bot.send_message(chat_id=user.chat_id_, text=message, reply_markup=q_keyboard)
        debug(flag="MSG", text=str(user.chat_id_) + ": " + message + "\n")
    except TelegramError as error:
        if error.message == 'Unauthorized':
            user.pause()
    user.set_q_idle(True)

    # Check if there is a reason to queue again.
    if not user.auto_queue_:
        return

    # Calculate seconds until question is due.
    next_day = user.set_next_block()
    if user.next_block is None:
        return finished(user, job_queue)
    element = user.next_block[2]
    day_offset = next_day - user.day_
    time_t = calc_block_time(element["time"])
    due = calc_delta_t(time_t, day_offset, user.timezone_)

    debug('QUEUE', 'next block in ' + str(due) + ' seconds. User: ' + str(user.chat_id_), log=True)
    new_job = Job(queue_next, due, repeat=False, context=[user, job_queue])
    job_queue._put(new_job)
    return


# This function returns the next
# question meant for the user.
# If the block is complete None is returned.
def find_next_question(user):
    q_set = user.q_set_
    try:
        q_day = q_set[user.pointer_]
        q_block = q_day["blocks"][user.block_]
        element = q_block["questions"]
        user.increase_question()
        while not user.check_requirements(element[user.question_]):
            store_answer(user, '', element[user.question_], None)
            user.increase_question()
        question = element[user.question_]
        message = parse_question(user, element[user.question_])
        return message, question
    except IndexError:
        return None, None


# This function returns the ReplyKeyboard for the user.
# Either the ones from the json file are used or
# more complex ones are generated in survey/keyboard_presets.py
def get_keyboard(choice, user):
    if choice == []:
        return ReplyKeyboardRemove()

    # -------- Place to register dynamic keyboards -------- #
    if choice[0][0] == 'KB_TIMEZONE':
        return ReplyKeyboardMarkup(kb_presets.generate_timezone_kb(user.country_))

    try:
        keyboard = ReplyKeyboardMarkup(CUSTOM_KEYBOARDS[choice[0][0]])
    except KeyError:
        keyboard = ReplyKeyboardMarkup(choice)

    return keyboard


# If the command FORCE_KB_REPLY is set in json the
# answer is checked if it is really a choice
# from the ReplyKeyboard.
def valid_answer(question, message, user):
    commands = question['commands']
    if ['FORCE_KB_REPLY'] not in commands or question['choice'] == []:
        return True

    try:
        choice = CUSTOM_KEYBOARDS[question['choice'][0][0]]
    except KeyError:
        if question['choice'][0][0] == 'KB_TIMEZONE':
            choice = kb_presets.generate_timezone_kb(user.country_)
        else:
            choice = question['choice']

    if [message] in choice:
        return True
    else:
        return False


# This functions handles the very last question.
# It allows the user to finish its question within
# 24 hours. Afterwards finalize() is called.
def finished(user, job_queue):
    user.last_ = True
    new_job = Job(finalize, 86400, repeat=False, context=user)
    job_queue._put(new_job)
    return


# If the user reaches this function he has successfully
# completed the survey. The clean up is done here
# and the he gets set to passive.
def finalize(bot: Bot, job: Job):
    user = job.context
    user.set_active = False
    user.set_question(0xFFFF)
    user.set_block(0xFFFF)
    user.set_pointer(0xFFFF)

    srcfile = 'survey/data_incomplete/' + str(user.chat_id_) + '.csv'
    dstfile = 'survey/data_complete/' + str(user.chat_id_) + '.csv'
    shutil.copyfile(srcfile, dstfile)
    return


def parse_question(user, question):
    exp = u'<<(.*?)\|(.*?)\|(.*?)>>'
    sol = re.findall(exp, question["text"])
    message = question["text"]
    for element in sol:
        element = list(element)
        try:
            replacement = survey_function(user, user.data_set_[element[1]], element[2])
            message = question["text"].replace("<<" + element[0] + "|" + element[1] + "|" + element[2] + ">>",
                                               replacement)
        except KeyError:
            print("The structure" + str(element[1]) + "is unknown!")

    return message


def continue_survey(user, bot, job_queue):
    user.active_ = True
    q_set = user.q_set_
    q_day = q_set[user.pointer_]
    q_block = q_day["blocks"][user.block_]
    question = q_block["questions"][user.question_]

    if question is not None:
        message = parse_question(user, question)
        q_keyboard = get_keyboard(question["choice"], user)
        try:
            bot.send_message(chat_id=user.chat_id_, text=message, reply_markup=q_keyboard)
            debug(flag="MSG", text=str(user.chat_id_) + ": " + message + "\n")
        except TelegramError as error:
            if error.message == 'Unauthorized':
                user.pause()
        user.set_q_idle(True)

    if user.job_ is None and ["MANDATORY"] not in q_block["settings"]:
        user.block_complete_ = True
        next_day = user.set_next_block()
        if next_day is None:
            finished(user, job_queue)
            return
        element = user.next_block[2]
        day_offset = next_day - user.day_
        time_t = calc_block_time(element["time"])
        due = calc_delta_t(time_t, day_offset, user.timezone_)

        debug('QUEUE', 'next block in ' + str(due) + ' seconds. User: ' + str(user.chat_id_), log=True)
        new_job = Job(queue_next, due, repeat=False, context=[user, job_queue])
        user.job_ = new_job
        job_queue._put(new_job)
    return


# This function gets called at program start to load in
# all users from the DB. This function ensures that random
# crashes of the program are not an issue and no data loss occurs.
def initialize_participants(job_queue: JobQueue):
    user_map = DataSet()
    try:
        db = sqlite3.connect('survey/participants.db')
        cursor = db.cursor()
        cursor.execute("SELECT * FROM participants ORDER BY (ID)")
        participants = cursor.fetchall()
        for row in participants:
            user = Participant(row[1], init=False)
            user.conditions_ = pickle.loads(row[2])
            user.data_set_ = pickle.loads(row[0])
            user.timezone_ = row[3]
            user.country_ = row[4]
            user.gender_ = row[5]
            user.language_ = row[6]
            user.question_ = row[7]
            user.age_ = row[8]
            user.day_ = row[9]
            user.q_idle_ = row[10]
            user.active_ = row[11]
            user.block_ = row[12]
            user.pointer_ = row[13]
            user_map.participants[row[1]] = user
            if user.language_ != '':
                q_set = user_map.return_question_set_by_language(user.language_)
                user.q_set_ = q_set
                if user.country_ != '' and user.timezone_ != '' and user.gender_ != '':
                    user.set_next_block()
                    next_day = user.set_next_block()
                    if next_day is None and user.active_ and user.pointer_ > -1:
                        finished(user, job_queue)
                        continue
                    element = user.next_block[2]
                    day_offset = next_day - user.day_
                    time_t = calc_block_time(element["time"])
                    due = calc_delta_t(time_t, day_offset, user.timezone_)

                    debug('QUEUE', 'next block in ' + str(due) + ' seconds. User: ' + str(user.chat_id_), log=True)
                    new_job = Job(queue_next, due, repeat=False, context=[user, job_queue])
                    job_queue._put(new_job)
    except sqlite3.Error as error:
        print(error)
    return user_map
