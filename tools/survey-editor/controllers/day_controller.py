import json
import os
import re
from PyQt5.QtCore import QObject, pyqtSlot

# The controller class performs any logic and sets data in the model.
from model.survey import Block, Question
from resources.languages import iso_639_choices


class DayController(QObject):
    def __init__(self, model):
        super().__init__()
        self._model = model
        self._view = None

    def init_project(self):
        self._view.disable_lang()
        self.init_config()
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
