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
            self.questions.append(question)
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
            self.blocks.append(block)
        else:
            print("Object: " + block + " should be of type Block")

    def get_object(self):
        return OrderedDict([("day", self.day),
                            ("meta", self.meta),
                            ("blocks", self.blocks)])

    def info(self):
        return "#" + str(self.day) + " | " + str(len(self.blocks)) + " blocks"


class Survey:
    def __init__(self, survey, language):
        self.language = language
        self.days = []
        if survey is not None:
            try:
                for day in survey:
                    d = Day()
                    d.set_day(day["day"])
                    d.set_meta(day["meta"])
                    for block in day["blocks"]:
                        b = Block()
                        b.set_time(block["time"])
                        b.set_meta(block["meta"])
                        b.set_settings(block["settings"])
                        for question in block["questions"]:
                            q = Question()
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
        print(self)

    def info(self):
        pass

    def add_day(self, day):
        if isinstance(day, Day):
            self.days.append(day)
        else:
            print("Object: " + day + " should be of type Day")

    def get_object(self):
        return self.days


class Model:
    def __init__(self):
        self.dir = ""
        self.languages = []
        self.surveys = {}
        # Todo: Find a place to define default language
        self.default_language = "de"

    def add_survey(self, json_survey, language):
        self.languages.append(language)
        survey = Survey(json_survey, language)
        self.surveys[language] = survey
