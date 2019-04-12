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
        self._ui.save_button.clicked.connect(self.save_and_return)
        self._ui.cancel_button.clicked.connect(self.cancel_and_return)
        self._ui.custom_add_button.clicked.connect(self.add_custom_keyboard)
        self._ui.custom_delete_button.clicked.connect(self.delete_custom_keyboard)
        self._ui.language_box.currentIndexChanged.connect(self.change_default_language)
        self._ui.editor_box.currentIndexChanged.connect(self.change_editor_mode)

    def populate(self):
        index = self._model.languages.index(self._model.default_language)
        self._ui.language_field.setText(self._model.default_language)
        self._ui.language_box.addItems(self._model.languages)
        self._ui.language_box.setCurrentIndex(index)
        self._ui.name_field.setText(self._model.project_name)
        self._ui.editor_field.setText(self._model.editor_mode)
        self.fill_custom_keyboards()

    def change_default_language(self):
        self._model.default_language = self._ui.language_box.currentText()
        self._ui.language_field.setText(self._model.default_language)
        self._model.update_config_file()

    def change_editor_mode(self):
        self._model.editor_mode = self._ui.editor_box.currentText()
        self._ui.editor_field.setText(self._model.editor_mode)
        self._model.update_config_file()

    def fill_custom_keyboards(self):
        self._ui.custom_list.clear()
        self._ui.custom_list.addItems(self._model.custom_keyboards)

    def add_custom_keyboard(self):
        if self._ui.custom_field == "":
            return
        keyboard = self._ui.custom_field.text()
        if keyboard in self._model.custom_keyboards:
            self._ui.custom_field.setText("")
            return
        self._model.custom_keyboards.append(keyboard)
        self._ui.custom_field.clear()
        self._model.update_config_file()
        self.fill_custom_keyboards()

    def delete_custom_keyboard(self):
        if not self._ui.custom_list.selectedItems():
            return
        index = self._ui.custom_list.currentRow()
        keyboard = self._ui.custom_list.item(index).text()
        self._model.custom_keyboards.remove(keyboard)
        self._model.update_config_file()
        self.fill_custom_keyboards()

    def save_and_return(self):
        self._model.project_name = self._ui.name_field.text()
        self._model.update_config_file()
        self.parent().setCurrentIndex(0)

    def cancel_and_return(self):
        self.parent().setCurrentIndex(0)
