import json
from collections import OrderedDict
import random

SAMPLE_DATA = [
    ["Considering your complete experience with our company, how likely would you be to recommend us to a friend "
     "or colleague?", [["1"], ["2"], ["3"], ["4"]], ["5"]],

    ["Are you in any physical pain?", [["Yes"], ["No"]]],

    ["How much did you drink today (in l)?", []],

    ["How much time did you spent studying today? (in h)", []]
]


class Question:
    def __init__(self, text="", choice=[], condition_required=[], condition=[], commands=[], meta=[], status=[]):
        self.text = text
        self.choice = choice
        self.condition_required = condition_required
        self.condition = condition
        self.commands = commands
        self.meta = meta
        self.status = status

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

    def get_object(self):
        return OrderedDict([("text", self.text),
                            ("choice", self.choice),
                            ("condition_required", self.condition_required),
                            ("condition", self.condition),
                            ("commands", self.commands)])


class Block:
    def __init__(self, time="", settings=[], meta="", questions=[]):
        self.time = time
        self.settings = settings
        self.meta = meta
        self.questions = questions

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
    def __init__(self, day="", meta="", blocks=[]):
        self.day = day
        self.meta = meta
        self.blocks = blocks

    def set_day(self, day):
        if isinstance(day, str):
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
        day = Day(str(i))
        survey.add_day(day)
        for j in range(nr_of_blocks):
            block = Block(t_map[j])
            day.add_block(block)
            for k in range(nr_of_questions):
                pick = random.choice(sample_data)
                question = Question(pick[0], pick[1])
                block.add_question(question)

    return survey


# data = random.choice(SAMPLE_DATA)
#
# question1 = Question()
# question1.set_text(data[0])
# question1.set_choice(data[1])
# question2 = Question()
# question3 = Question()
# block = Block()
# day = Day()
# survey = Survey()
#
# block.add_question(question1)
# block.add_question(question2)
# block.add_question(question3)
# day.add_block(block)
# survey.add_day(day)
#
# question4 = Question()
# question5 = Question()
# question6 = Question()
# block2 = Block()
# day2 = Day()
#
# block2.add_question(question4)
# block2.add_question(question5)
# block2.add_question(question6)
# day2.add_block(block2)
# survey.add_day(day2)

survey = generate_sample_survey(3, 3, 3, SAMPLE_DATA)

print(json.dumps(survey.get_object()))
