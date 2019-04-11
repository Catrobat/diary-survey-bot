"""
diary-survey-bot | survey-editor

Software-Design: Philipp Feldner
Documentation: https://github.com/Catrobat/diary-survey-bot

Qt version: 5.12.1
"""

from PyQt5.QtWidgets import QWidget
from views.settings_view_ui import Ui_Settings


# The view class should mainly contain code to handle events and trigger
# events in/from the user interface.
# related .ui file in ../qt/settings.ui


class SettingsView(QWidget):
    def __init__(self, model, settings_controller):
        super().__init__()

        self._model = model
        self._controller = settings_controller
        self._ui = Ui_Settings()
        self._ui.setupUi(self)

    def populate(self):
        pass  # todo
