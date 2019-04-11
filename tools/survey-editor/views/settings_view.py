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
        self._ui.language_field.setText(self._model.default_language)
        self._ui.name_field.setText(self._model.project_name)
        self._ui.language_box.addItems(self._model.languages)
        self._ui.editor_field.setText(self._model.editor_mode)
        self.fill_custom_keyboards()

    def fill_custom_keyboards(self):
        pass  # Todo

    def add_custom_keyboard(self):
        pass  # Todo

    def delete_custom_keyboard(self):
        pass  # Todo

