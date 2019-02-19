"""
diary-survey-bot

Developed in association with Uni-Graz.
Idea: Lisa Eckerstorfer MSc.
Supervisor: Univ.-Prof. Dr.phil. Dipl.-Psych. Katja Corcoran

Software-Design: Philipp Feldner (Computer Science Student TU Graz)
Documentation: https://github.com/philippfeldner/diary-survey-bot

Telegram API:
https://github.com/python-telegram-bot/python-telegram-bot
"""


from telegram import Bot, Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import TelegramError

from survey.data_set import DataSet
from survey.questions import initialize_participants
from survey.questions import question_handler
from survey.questions import continue_survey
from survey.participant import Participant

from survey.keyboard_presets import languages

from admin.settings import INFO_TEXT
from admin.settings import STOP_TEXT
from admin.settings import DEFAULT_LANGUAGE
from admin.settings import DELETE

import os

data_set = None


def start(bot: Bot, update: Update, job_queue):
    global data_set
    if update.message.chat_id not in data_set.participants:
        reply_markup = ReplyKeyboardMarkup(languages)
        try:
            bot.send_message(chat_id=update.message.chat_id, text="Please choose a language:", reply_markup=reply_markup)
        except TelegramError as error:
            if error.message == 'Unauthorized':
                return
        participant = Participant(update.message.chat_id)
        data_set.participants[update.message.chat_id] = participant
    else:
        user = data_set.participants[update.message.chat_id]
        # A user that has already completed the survey tries to do it again.
        if user.pointer_ == 0xFFFF:
            return
        continue_survey(user, bot, job_queue)


def delete(bot: Bot, update: Update):
    if not DELETE:
        return

    global data_set
    chat_id = update.message.chat_id
    user = data_set.participants[update.message.chat_id]
    user.active_ = False
    user.delete_participant()

    try:
        os.remove('survey/data_incomplete/' + str(user.chat_id_) + '.csv')
    except OSError:
        pass

    try:
        os.remove('survey/data_complete/' + str(user.chat_id_) + '.csv')
    except OSError:
        pass

    del data_set.participants[update.message.chat_id]
    try:
        bot.send_message(chat_id=chat_id, text="Successfully deleted DB entry and user data. To restart enter /start")
    except TelegramError as error:
        if error.message == 'Unauthorized':
            user.pause()


def stop(bot: Bot, update: Update):
    global data_set
    chat_id = update.message.chat_id
    user = data_set.participants[update.message.chat_id]
    user.pause()
    try:
        message = STOP_TEXT[user.language_]
        bot.send_message(chat_id=chat_id, text=message, reply_markup=ReplyKeyboardRemove())
    except KeyError:
        message = STOP_TEXT[DEFAULT_LANGUAGE]
        bot.send_message(chat_id=chat_id, text=message, reply_markup=ReplyKeyboardRemove())
    except TelegramError as error:
        if error.message == 'Unauthorized':
            user.pause()


def msg_handler(bot, update, job_queue):
    global data_set
    question_handler(bot, update, data_set, job_queue)
    

def info(bot: Bot, update: Update):
    global data_set
    try:
        user = data_set.participants[update.message.chat_id]
        message = INFO_TEXT[user.language_]
        try:
            bot.sendMessage(update.message.chat_id, text=message)
        except TelegramError:
            return
    except KeyError:
        message = INFO_TEXT[DEFAULT_LANGUAGE]
        try:
            bot.sendMessage(update.message.chat_id, text=message)
        except TelegramError:
            return


def main():


    # Enter your own token here
    updater = Updater("739345028:AAFc0t60KK-jqFI3DbA9Iz7irKICJCcGEIA")

    dp = updater.dispatcher
    global data_set
    data_set = initialize_participants(dp.job_queue)
    dp.add_handler(CommandHandler('start', start, pass_job_queue=True))
    dp.add_handler(CommandHandler('delete_me', delete))
    dp.add_handler(CommandHandler('stop', stop))
    dp.add_handler(CommandHandler('info', info))
    dp.add_handler(MessageHandler(Filters.text, callback=msg_handler, pass_job_queue=True))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()


