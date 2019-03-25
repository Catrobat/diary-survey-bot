"""
diary-survey-bot | survey-editor

Software-Design: Philipp Feldner
Documentation: https://github.com/Catrobat/diary-survey-bot

Qt version: 5.12.1
"""

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







