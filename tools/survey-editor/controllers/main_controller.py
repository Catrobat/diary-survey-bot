import json
import re

import os
from PyQt5.QtCore import QObject, pyqtSlot


# The controller class performs any logic and sets data in the model.
class MainController(QObject):
    def __init__(self, model):
        super().__init__()
        self._model = model
        self._view = None

    def init_project(self):
        # Todo: add handling of some config.json file
        regex = re.compile('(question_set_..\.json)')
        root_dir = self._model.dir

        for root, dirs, files in os.walk(root_dir):
            for file in files:
                if regex.match(file):
                    try:
                        language = file.split("_")[2].split(".")[0]
                        with open(root_dir + "/" + file) as fp:
                            survey = json.load(fp)
                            self._model.add_survey(survey, language)
                    except ValueError as e:
                        # Todo: Error handling
                        print(e)

        day_list = []
        for day in self._model.surveys[self._model.default_language].days:
            day_list.append(day.info())

        self._model.u_survey = self._model.surveys[self._model.default_language]
        self._view.fill_day_list(day_list)



