import json
import os
import re
from PyQt5.QtCore import QObject, pyqtSlot

# The controller class performs any logic and sets data in the model.


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
                    except ValueError as e:
                        # Todo: Error handling
                        print(e)
                        return -1

        day_list = []
        for day in self._model.surveys[self._model.default_language].days:
            day_list.append(day.info())

        self._model.u_survey = self._model.surveys[self._model.default_language]
        self._view.fill_day_list(day_list)
        self._view.fill_lang_list(lang_list)
        self._view.fill_project_list(self._model.recent_projects)

    def init_config(self):
        try:
            with open(self._model.dir + "/config.json") as fp:
                config = json.load(fp)
        except FileExistsError as e:
            # Todo: Error handling
            print(e)
            return -1

        self._model.default_language = config["default-language"]
        self._model.recent_projects = config["recent-projects"]
        self._model.time_slots = config["time-slots"]
        self._model.keyboard_templates = config["keyboard-templates"]
        self._model.question_templates = config["question-templates"]
        self._model.strict_time_slots = config["strict-time-slots"]
