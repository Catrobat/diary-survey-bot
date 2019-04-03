"""
diary-survey-bot | survey-editor

Software-Design: Philipp Feldner
Documentation: https://github.com/Catrobat/diary-survey-bot

Qt version: 5.12.1
"""
import copy
import json
import os
import re

from PyQt5.QtCore import QObject

# The controller class performs any logic and sets data in the model.

from model.survey import Block, Question, Survey
from resources.languages import iso_639_choices


class DayController(QObject):
    def __init__(self, model):
        super().__init__()
        self._model = model
        self._view = None

    def init_project(self):
        self._view.disable_lang()
        regex = re.compile('(question_set_..\.json)')
        root_dir = self._model.dir
        self._model.recent_projects.append(root_dir)
        lang_list = []

        for root, dirs, files in os.walk(root_dir):
            for file in files:
                if regex.match(file):
                    try:
                        language = file.split("_")[2].split(".")[0]
                        lang_list.append(language)
                        with open(root_dir + "/" + file) as fp:
                            survey = json.load(fp)
                            self._model.add_survey(survey, language)
                            self._model.conditions[language] = []
                    except ValueError as e:
                        # Todo: Error handling
                        print(e)
                        return -1

        if not lang_list:
            print("e")
            pass  # there are no files - new project! #todo

        self.init_config()
        self._model.init_condition_coordinates()
        self._model.load_templates()

        day_list = []
        self._model.languages = lang_list
        for day in self._model.surveys[self._model.default_language].days:
            day_list.append(day.info())

        self._view.fill_day_list(day_list)

        lang_info = []
        for item in lang_list:
            lang_info.append(item + " -> " + iso_639_choices[item])
        self._view.fill_lang_list(lang_info)
        self._view.fill_project_list(self._model.recent_projects)
        self._view.enable_days()

    def init_config(self):
        try:
            with open(self._model.dir + "/config.json") as fp:
                config = json.load(fp)
        except FileExistsError as e:
            # Todo: Error handling
            print(e)
            return -1

            # todo
            # self._model.default_language = config["default-language"]
            # self._model.recent_projects = config["recent-projects"]
            # self._model.time_slots = config["time-slots"]
            # self._model.keyboard_templates = config["keyboard-templates"]
            # self._model.question_templates = config["question-templates"]
            # self._model.strict_time_slots = config["strict-time-slots"]

    def build_day_template(self, key, days):
        template = {}
        for lang in days:
            template[lang] = days[lang].get_object()
        self._model.add_day_template(key, template)

    def load_day_template(self, key):
        template = self._model.day_templates[key]
        for lang in template:
            self._model.days[lang].set_meta(template[lang]["meta"])
            self._model.days[lang].set_day(0)  # todo
            self._model.days[lang].blocks = []
            for b in template[lang]["blocks"]:
                block = Block()
                block.set_meta(b["meta"])
                block.set_settings(b["settings"])
                block.set_survey(self._model.surveys[lang])
                block.set_day(self._model.days[lang])
                for item in b["questions"]:
                    question = Question()
                    question.set_text(item["text"])
                    question.set_choice(item["choice"])
                    question.set_condition_required(item["condition_required"])
                    question.set_condition([])
                    question.set_commands(item["commands"])
                    question.set_meta(item["meta"])
                    question.set_variable(item["variable"])
                    question.set_block(block)
                    question.set_day(self._model.days[lang])
                    question.set_survey(self._model.surveys[lang])
                    block.add_question(question)
                self._model.days[lang].add_block(block)

    def set_day(self, day):
        if any(x.day == day for x in self._model.surveys[self._model.default_language].days):
            return False  # todo error handling
        for lang in self._model.languages:
            self._model.days[lang].day = day
        return True

    def move_day(self, index, direction):
        max_index = len(self._model.surveys[self._model.default_language].days) - 1
        if index + direction < 0 or index + direction > max_index:
            return False
        for lang in self._model.languages:
            self._model.surveys[lang].days[index + direction].day, self._model.surveys[lang].days[index].day = \
                self._model.surveys[lang].days[index].day, self._model.surveys[lang].days[index + direction].day

            self._model.surveys[lang].days[index + direction], self._model.surveys[lang].days[index] = \
                self._model.surveys[lang].days[index], self._model.surveys[lang].days[index + direction]
        return True

    def shift_day(self, index, direction):
        end = len(self._model.surveys[self._model.default_language].days)
        start = index
        if index == 0:
            minimum = 1
        else:
            minimum = self._model.surveys[self._model.default_language].days[index - 1].day + 1

        if minimum == self._model.surveys[self._model.default_language].days[index].day and direction == -1:
            return False

        for lang in self._model.languages:
            for i in range(start, end):
                self._model.surveys[lang].days[i].day += direction

    def add_lang(self, lang):
        self._model.languages.append(lang)
        self._model.conditions[lang] = []
        if not self._model.languages:
            survey = Survey(None, lang)
            self._model.surveys[lang] = survey
            self._model.update_surveys()
            return
        default = copy.deepcopy(self._model.surveys[self._model.default_language])
        survey = Survey(default.get_object(), lang)
        for day in survey.days:
            for block in day.blocks:
                for question in block.questions:
                    question.set_text("--TRANSLATE--")
                    question.set_choice([])
                    question.set_condition_required([])
                    question.set_condition([])

        self._model.surveys[lang] = survey
        self._model.update_surveys()

    def add_lang_to_templates(self, lang):
        if self._model.day_templates != {}:
            for key in self._model.day_templates:
                template = self._model.day_templates[key]
                template[lang] = copy.deepcopy(template[self._model.default_language])
                for block in template[lang]["blocks"]:
                    for question in block["questions"]:
                        question["text"] = "--TRANSLATE--"
                        question["condition"] = []
                        question["condition_required"] = []
                        question["choice"] = []

        if self._model.block_templates != {}:
            for key in self._model.block_templates:
                template = self._model.block_templates[key]
                template[lang] = copy.deepcopy(template[self._model.default_language])
                for question in template[lang]["questions"]:
                    question["text"] = "--TRANSLATE--"
                    question["condition"] = []
                    question["condition_required"] = []
                    question["choice"] = []

        if self._model.question_templates != {}:
            for key in self._model.question_templates:
                question = self._model.question_templates[key]
                question[lang] = copy.deepcopy(question[self._model.default_language])
                question[lang]["text"] = "--TRANSLATE--"
                question[lang]["condition"] = []
                question[lang]["condition_required"] = []
                question[lang]["choice"] = []

        self._model.update_templates()

    def delete_language(self, lang):
        self._model.languages.remove(lang)
        self._model.surveys.pop(lang, None)
        self._model.days.pop(lang, None)
        self._model.blocks.pop(lang, None)
        self._model.questions.pop(lang, None)
        self._model.conditions.pop(lang, None)
        file = self._model.dir + "/question_set_" + lang + ".json"
        os.remove(file)

    def delete_lang_from_templates(self, lang):
        for key in self._model.day_templates:
            del self._model.day_templates[key][lang]
        for key in self._model.block_templates:
            del self._model.block_templates[key][lang]
        for key in self._model.question_templates:
            del self._model.question_templates[key][lang]
        self._model.update_templates()
