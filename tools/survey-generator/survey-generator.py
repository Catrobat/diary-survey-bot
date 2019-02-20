"""
diary-survey-bot 2.0

Software-Design: Philipp Feldner
Documentation: https://github.com/Catrobat/diary-survey-bot

Telegram API:
https://github.com/python-telegram-bot/python-telegram-bot
"""

import json
from collections import OrderedDict
import random

SAMPLE_DATA = [
    ["Considering your complete experience with our company, how likely would you be to recommend us to a friend "
     "or colleague?", [["1"], ["2"], ["3"], ["4"]], ["5"]],

    ["Are you in any physical pain?", [["Yes"], ["No"]]],

    ["How much did you drink today (in l)?", []],

    ["How much time did you spent studying today? (in h)", []],

    ["What is your gender?", [["male"], ["female"]]],

    ["Do you have siblings?", [["Yes"], ["No"]]],

    ["Who wrote the book: Brave New World?", [["Aldous Huxley"], ["George Orwell"]]],

    ["Do you have any programming experience?", [["Yes"], ["No"]]]
]


class Question:
    def __init__(self):
        self.text = ""
        self.choice = []
        self.condition_required = []
        self.condition = []
        self.commands = []
        self.meta = ""
        self.status = ""
        self.variable = ""

    # Todo: proper format checking
    def set_text(self, text):
        if isinstance(text, str):
            self.text = text
        else:
            print("text: " + text + " should be a string.")

    def set_choice(self, choice):
        if isinstance(choice, list):
            self.choice = choice
        else:
            print("choice: " + choice + " should be defined in nested lists. ")

    def set_condition_required(self, condition_required):
        if isinstance(condition_required, list):
            self.condition_required = condition_required
        else:
            print("condition_required: " + condition_required + " should be defined as nested lists. ")

    def set_condition(self, condition):
        if isinstance(condition, list):
            self.condition = condition
        else:
            print("condition: " + condition + " should be defined as nested lists. ")

    def set_commands(self, commands):
        if isinstance(commands, list):
            self.commands = commands
        else:
            print("commands: " + commands + " should be defined as nested lists. ")

    def set_meta(self, meta):
        if isinstance(meta, str):
            self.meta = meta
        else:
            print("meta: " + meta + " should be a string.")

    def set_status(self, status):
        if isinstance(status, str):
            self.status = status
        else:
            print("status: " + status + " should be a string.")

    def set_variable(self, variable):
        if isinstance(variable, str):
            self.variable = variable
        else:
            print("variable: " + variable + " should be a string.")

    def get_object(self):
        return OrderedDict([("text", self.text),
                            ("choice", self.choice),
                            ("condition_required", self.condition_required),
                            ("condition", self.condition),
                            ("commands", self.commands),
                            ("variable", self.variable)])


class Block:
    def __init__(self):
        self.time = ""
        self.settings = []
        self.meta = ""
        self.questions = []

    def set_time(self, time):
        if isinstance(time, str):
            self.time = time
        else:
            print("time: " + time + " should be a string.")

    def set_settings(self, settings):
        if isinstance(settings, list):
            self.settings = settings
        else:
            print("settings: " + settings + " should be defined as nested lists. ")

    def set_meta(self, meta):
        if isinstance(meta, str):
            self.meta = meta
        else:
            print("meta: " + meta + " should be a string.")

    def add_question(self, question):
        if isinstance(question, Question):
            self.questions.append(question.get_object())
        else:
            print("Object: " + question + " should be of type Question")

    def get_object(self):
        return OrderedDict([("time", self.time),
                            ("settings", self.settings),
                            ("meta", self.meta),
                            ("questions", self.questions)])


class Day:
    def __init__(self):
        self.day = -1
        self.meta = ""
        self.blocks = []

    def set_day(self, day):
        if isinstance(day, int):
            self.day = day
        else:
            print("day: " + day + " should be a string.")

    def set_meta(self, meta):
        if isinstance(meta, str):
            self.meta = meta
        else:
            print("meta: " + meta + " should be a string.")

    def add_block(self, block):
        if isinstance(block, Block):
            self.blocks.append(block.get_object())
        else:
            print("Object: " + block + " should be of type Block")

    def get_object(self):
        return OrderedDict([("day", self.day),
                            ("meta", self.meta),
                            ("blocks", self.blocks)])


class Survey:
    def __init__(self):
        self.days = []

    def add_day(self, day):
        if isinstance(day, Day):
            self.days.append(day.get_object())
        else:
            print("Object: " + day + " should be of type Day")

    def get_object(self):
        return self.days


def generate_sample_survey(nr_of_days, nr_of_blocks, nr_of_questions, sample_data):
    t_map = {0: "0800", 1: "1200", 2: "1600", 3: "2000"}
    survey = Survey()
    for i in range(nr_of_days):
        day = Day()
        day.set_day(i + 1)
        for j in range(nr_of_blocks):
            block = Block()
            block.set_time(t_map[j])
            for k in range(nr_of_questions):
                pick = random.choice(sample_data)
                question = Question()
                question.set_text(pick[0])
                question.set_choice(pick[1])
                question.set_variable("question" + str(k))
                block.add_question(question)
            day.add_block(block)
        survey.add_day(day)

    return survey


# Todo write a proper argparse and possibly add questions for first and last day/block
survey = generate_sample_survey(2, 2, 2, SAMPLE_DATA)
print(json.dumps(survey.get_object()))
