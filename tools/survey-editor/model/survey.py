import json
from collections import OrderedDict


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

        self.survey = None
        self.day = None
        self.block = None

    def set_survey(self, survey):
        if isinstance(survey, Survey):
            self.survey = survey
        else:
            print("survey should be of type Survey.")

    def set_day(self, day):
        if isinstance(day, Day):
            self.day = day
        else:
            print("day should be of type Day.")

    def set_block(self, block):
        if isinstance(block, Block):
            self.block = block
        else:
            print("block should be of type Block.")

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
                            ("variable", self.variable)])

    def info(self):
        return "#" + str(self.block.questions.index(self) + 1) + " | " + self.text


class Block:
    def __init__(self):
        self.time = ""
        self.settings = []
        self.meta = ""
        self.questions = []

        self.survey = None
        self.day = None

    def set_survey(self, survey):
        if isinstance(survey, Survey):
            self.survey = survey
        else:
            print("survey should be of type Survey.")

    def set_day(self, day):
        if isinstance(day, Day):
            self.day = day
        else:
            print("day should be of type Day.")

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
            self.questions.append(question)
        else:
            print("Object: " + question + " should be of type Question")

    def get_object(self):
        return OrderedDict([("time", self.time),
                            ("settings", self.settings),
                            ("meta", self.meta),
                            ("questions", self.questions)])

    def get_number_of_questions(self):
        return len(self.questions)

    def info(self):
        return self.time + " | " + str(len(self.questions)) + " questions"


class Day:
    def __init__(self):
        self.day = -1
        self.meta = ""
        self.blocks = []

        self.survey = None

    def set_survey(self, survey):
        if isinstance(survey, Survey):
            self.survey = survey
        else:
            print("survey should be of type Survey.")

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
            self.blocks.append(block)
        else:
            print("Object: " + block + " should be of type Block")

    def get_object(self):
        return OrderedDict([("day", self.day),
                            ("meta", self.meta),
                            ("blocks", self.blocks)])

    def get_number_of_questions(self):
        amount = 0
        for block in self.blocks:
            amount += block.get_number_of_questions()
        return amount

    def info(self):
        return "#" + str(self.day) + " | " + str(len(self.blocks)) + " blocks | " + \
               str(self.get_number_of_questions()) + " questions"


class Survey:
    def __init__(self, survey, language):
        self.language = language
        self.days = []
        if survey is not None:
            try:
                for day in survey:
                    d = Day()
                    d.set_survey(self)
                    d.set_day(day["day"])
                    d.set_meta(day["meta"])
                    for block in day["blocks"]:
                        b = Block()
                        b.set_survey(self)
                        b.set_day(d)
                        b.set_time(block["time"])
                        b.set_meta(block["meta"])
                        b.set_settings(block["settings"])
                        for question in block["questions"]:
                            q = Question()
                            q.set_survey(self)
                            q.set_day(d)
                            q.set_block(b)
                            q.set_text(question["text"])
                            q.set_meta(question["meta"])
                            q.set_choice(question["choice"])
                            q.set_condition(question["condition"])
                            q.set_condition_required(question["condition_required"])
                            q.set_commands(question["commands"])
                            q.set_variable(question["variable"])
                            b.add_question(q)
                        d.add_block(b)
                    self.add_day(d)
            except KeyError as e:
                print(e)

    def info(self):
        pass

    def add_day(self, day):
        if isinstance(day, Day):
            self.days.append(day)
        else:
            print("Object: " + day + " should be of type Day")

    def get_object(self):
        return self.days

    def get_number_of_questions(self):
        amount = 0
        for day in self.days:
            amount += day.get_number_of_questions()
        return amount


class Model:
    def __init__(self):
        self.dir = ""
        self.languages = []

        self.default_language = "de"
        self.recent_projects = ["/home/philipp/Development/Bachelorarbeit/diary-survey-bot/tools/survey-editor/survey"]
        self.time_slots = []
        self.strict_time_slots = True
        self.custom_keyboards = []

        self.keyboard_templates = []
        self.question_templates = []

        self.lang = ""
        self.surveys = {}
        self.days = {}
        self.blocks = {}
        self.questions = {}

    def set_days(self, index):
        for lang in self.languages:
            self.days[lang] = self.surveys[lang].days[index]

    def set_blocks(self, index):
        for lang in self.languages:
            self.blocks[lang] = self.days[lang].blocks[index]

    def set_questions(self, index):
        for lang in self.languages:
            self.questions[lang] = self.blocks[lang].questions[index]

    def add_survey(self, json_survey, lang):
        self.languages.append(lang)
        survey = Survey(json_survey, lang)
        self.surveys[lang] = survey

    def update_config_file(self):
        config = OrderedDict([("default-language", self.default_language),
                              ("recent-projects", self.recent_projects),
                              ("time-slots", self.time_slots),
                              ("custom-keyboard", self.custom_keyboards),
                              ("keyboard-templates", self.keyboard_templates),
                              ("question-templates", self.question_templates),
                              ("strict-time-slots", self.strict_time_slots)])

        try:
            with open(self.dir + "/config.json", "w") as fp:
                json.dump(config, fp)
        except FileExistsError as e:
            # Todo: Error handling
            print(e)
            return -1



