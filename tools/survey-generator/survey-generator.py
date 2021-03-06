"""
diary-survey-bot 2.0

Software-Design: Philipp Feldner
Documentation: https://github.com/Catrobat/diary-survey-bot

Telegram API:
https://github.com/python-telegram-bot/python-telegram-bot
"""
import argparse
import json
from collections import OrderedDict
import random

SAMPLE_DATA_EN = [
    ["Considering your complete experience with our company, how likely would you be to recommend us to a friend "
     "or colleague?", [["1"], ["2"], ["3"], ["4"], ["5"]],
     "Question about company experience.",
     "XP"],

    ["Are you in any physical pain?", [["Yes"], ["No"]],
     "Question about physical pain.",
     "PAIN"],

    ["How much did you drink today (in l)?", [],
     "Question about drinking.",
     "DRINK"],

    ["How much time did you spent studying today (in h)?", [],
     "Question about studying.",
     "STUDY"],

    ["What is your gender?", [["male"], ["female"]],
     "Question about gender.",
     "GENDER"],

    ["Do you have siblings?", [["Yes"], ["No"]],
     "Question about siblings.",
     "SIBLINGS"],

    ["Who wrote the book: Brave New World?", [["Aldous Huxley"], ["George Orwell"], ["Carl Sagan"]],
     "Question about author.",
     "AUTHOR"],

    ["Do you have any programming experience?", [["Yes"], ["No"]],
     "Question about programming.",
     "PROGRAMMING"],

    ["Choose a language!", [["German"], ["English"], ["Italian"]],
     "Question about language.",
     "LANGUAGE"]
]

SAMPLE_DATA_DE = [
    ["Wenn Sie Ihre gesammte Erfahrung mit unserer Firma in Betracht ziehen, wie wahrscheinlich ist es, dass Sie uns"
     "an einen Freund weiterempfehlen.", [["1"], ["2"], ["3"], ["4"], ["5"]],
     "Question about company experience.",
     "XP"],

    ["Habe Sie irgendwelche Schmerzen", [["Ja"], ["Nein"]],
     "Question about physical pain.",
     "PAIN"],

    ["Wieviel haben Sie heute getrunken (in l)?", [],
     "Question about drinking.",
     "DRINK"],

    ["Wieviel Zeit haben Sie heute mit lernen verbracht (in h)?", [],
     "Question about studying.",
     "STUDY"],

    ["Sind sie männlich oder weiblich?", [["männlich"], ["weiblich"]],
     "Question about gender.",
     "GENDER"],

    ["Haben Sie Geschwister?", [["Ja"], ["Nein"]],
     "Question about siblings.",
     "SIBLINGS"],

    ["Wer ist der Autor des Buches: Brave New World?", [["Aldous Huxley"], ["George Orwell"], ["Carl Sagan"]],
     "Question about author.",
     "AUTHOR"],

    ["Haben Sie Programmiererfahrung?", [["Yes"], ["No"]],
     "Question about programming.",
     "PROGRAMMING"],

    ["Wählen Sie eine Sprache!", [["Deutsch"], ["Englisch"], ["Italienisch"]],
     "Question about language.",
     "LANGUAGE"]
]

SAMPLE_DATA_IT = [
    ["Considerando la tua completa esperienza con la nostra azienda, quanto probabilmente vorresti raccomandarci "
     "ad un amico o collega?", [["1"], ["2"], ["3"], ["4"], ["5"]],
     "Question about company experience.",
     "XP"],

    ["Senti dolore?", [["Si"], ["No"]],
     "Question about physical pain",
     "PAIN"],

    ["Quanto hai bevuto oggi (in l)?", [],
     "Question about drinking.",
     "DRINK"],

    ["Quanto tempo hai studiato oggi (in h)?", [],
     "Question about studying.",
     "STUDY"],

    ["qual è il tuo genere?", [["maschio"], ["femina"]],
     "Question about gender.",
     "GENDER"],

    ["Hai fratelli?", [["Si"], ["No"]],
     "Question about siblings.",
     "SIBLINGS"],

    ["Chi ha scritto: Brave New World?", [["Aldous Huxley"], ["George Orwell"], ["Carl Sagan"]],
     "Question about author.",
     "AUTHOR"],

    ["Hai esperienza di programmazione?", [["Si"], ["No"]],
     "Question about programming.",
     "PROGRAMMING"],

    ["Scegli una lingua!", [["Tedesco"], ["Inglese"], ["Italiano"]],
     "Question about language.",
     "LANGUAGE"]
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

    def set_force_kb_reply(self):
        self.choice.append(["FORCE_KB_REPLY"])

    def get_object(self):
        return OrderedDict([("text", self.text),
                            ("choice", self.choice),
                            ("condition_required", self.condition_required),
                            ("condition", self.condition),
                            ("commands", self.commands),
                            ("meta", self.meta),
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
            print("day: " + day + " should be a int.")

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
    t_map = {0: "08:00", 1: "12:00", 2: "16:00", 3: "20:00"}
    survey_en = Survey()
    survey_de = Survey()
    survey_it = Survey()
    for i in range(nr_of_days):
        day_en = Day()
        day_de = Day()
        day_it = Day()
        day_en.set_day(i + 1)
        day_de.set_day(i + 1)
        day_it.set_day(i + 1)
        for j in range(nr_of_blocks):
            block_en = Block()
            block_de = Block()
            block_it = Block()
            block_en.set_time(t_map.setdefault(j, "12:00"))
            block_de.set_time(t_map.setdefault(j, "12:00"))
            block_it.set_time(t_map.setdefault(j, "12:00"))
            for k in range(nr_of_questions):
                index = random.randint(0, len(SAMPLE_DATA_DE) - 1)
                pick_en = SAMPLE_DATA_EN[index]
                pick_de = SAMPLE_DATA_DE[index]
                pick_it = SAMPLE_DATA_IT[index]

                question_en = Question()
                question_de = Question()
                question_it = Question()

                question_en.set_text(pick_en[0])
                question_en.set_choice(pick_en[1])
                question_en.set_meta(pick_en[2])
                question_en.set_variable(pick_en[3])

                question_de.set_text(pick_de[0])
                question_de.set_choice(pick_de[1])
                question_de.set_meta(pick_de[2])
                question_de.set_variable(pick_de[3])

                question_it.set_text(pick_it[0])
                question_it.set_choice(pick_it[1])
                question_it.set_meta(pick_it[2])
                question_it.set_variable(pick_it[3])

                block_en.add_question(question_en)
                block_de.add_question(question_de)
                block_it.add_question(question_it)
            day_en.add_block(block_en)
            day_de.add_block(block_de)
            day_it.add_block(block_it)
        survey_en.add_day(day_en)
        survey_de.add_day(day_de)
        survey_it.add_day(day_it
                          )
    return [("en", survey_en), ("de", survey_de), ("it", survey_it)]


# Simple survey generator that creates sample surveys in en/de/it
# You can add your own sample questions to the SAMPLE_DATA dictionaries.
# Usage: python survey-generator <number of days> <number of blocks per survey> <number of questions per block>
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("days", help="Enter the amount of days for your survey.", type=int)
    parser.add_argument("blocks", help="Enter the amount of blocks for your survey.", type=int)
    parser.add_argument("questions", help="Enter the amount of questions for your survey.", type=int)

    args = parser.parse_args()
    surveys = generate_sample_survey(args.days, args.blocks, args.questions, SAMPLE_DATA_DE)

    for survey in surveys:
        file = "question_set_" + survey[0] + ".json"
        with open(file, 'w', encoding="utf-8") as outfile:
            json.dump(survey[1].get_object(), outfile, indent=2)


if __name__ == '__main__':
    main()
