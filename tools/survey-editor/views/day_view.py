from PyQt5.QtWidgets import QWidget, QFileDialog
from views.day_view_ui import Ui_Day


# The view class should mainly contain code to handle events and trigger
# events in/from the user interface.
class DayView(QWidget):
    def __init__(self, model, day_controller):
        super().__init__()

        self._model = model
        self._controller = day_controller
        self._ui = Ui_Day()
        self._ui.setupUi(self)
        self._view = None

        self.day_frame_active = False
        self.block_view = None

        # remove later
        self._ui.project_list.addItem(
            "/home/philipp/Development/Bachelorarbeit/diary-survey-bot/tools/survey-editor/survey")

        # Register connections here
        self._ui.directory_tool.clicked.connect(self.change_root_dir)
        self._ui.day_list.itemSelectionChanged.connect(self.day_list_event)
        self._ui.block_list.itemSelectionChanged.connect(self.block_list_event)
        self._ui.project_list.itemSelectionChanged.connect(self.activate_project_options)
        self._ui.load_project_button.clicked.connect(self.load_project)
        self._ui.delete_project_button.clicked.connect(self.delete_project)
        self._ui.edit_block_button.clicked.connect(self.edit_block)
        self._ui.meta_save_button.clicked.connect(self.save_meta)
        self._ui.day_set_button.clicked.connect(self.set_day)

    def enable_days(self):
        self._ui.shift_down_button.setEnabled(True)
        self._ui.shift_up_button.setEnabled(True)
        self._ui.headline_days.setEnabled(True)
        self._ui.day_list.setEnabled(True)
        self._ui.new_day_button.setEnabled(True)
        self._ui.delete_day_button.setEnabled(True)

    def disable_days(self):
        self._ui.shift_down_button.setDisabled(True)
        self._ui.shift_up_button.setDisabled(True)
        self._ui.headline_days.setDisabled(True)
        self._ui.day_list.setDisabled(True)
        self._ui.new_day_button.setDisabled(True)
        self._ui.delete_day_button.setDisabled(True)

    def enable_day(self):
        self._ui.headline_day.setEnabled(True)
        self._ui.label_day.setEnabled(True)
        self._ui.day_field.setEnabled(True)
        self._ui.day_set_button.setEnabled(True)
        self._ui.label_meta.setEnabled(True)
        self._ui.meta_field.setEnabled(True)
        self._ui.label_blocks.setEnabled(True)
        self._ui.block_list.setEnabled(True)
        self._ui.new_block_button.setEnabled(True)
        self.day_frame_active = True

    def disable_day(self):
        self._ui.headline_day.setDisabled(True)
        self._ui.label_day.setDisabled(True)
        self._ui.day_field.setDisabled(True)
        self._ui.day_set_button.setDisabled(True)
        self._ui.label_meta.setDisabled(True)
        self._ui.meta_field.setDisabled(True)
        self._ui.label_blocks.setDisabled(True)
        self._ui.block_list.setEnabled(True)
        self._ui.new_block_button.setDisabled(True)
        self._ui.edit_block_button.setDisabled(True)
        self._ui.delete_block_button.setDisabled(True)
        self.day_frame_active = False

    def enable_lang(self):
        self._ui.headline_languages.setEnabled(True)
        self._ui.lang_add_button.setEnabled(True)
        self._ui.lang_delete_button.setEnabled(True)
        self._ui.iso_label.setEnabled(True)
        self._ui.lang_field.setEnabled(True)
        self._ui.lang_list.setEnabled(True)

    def disable_lang(self):
        self._ui.headline_languages.setDisabled(True)
        self._ui.lang_add_button.setDisabled(True)
        self._ui.lang_delete_button.setDisabled(True)
        self._ui.iso_label.setDisabled(True)
        self._ui.lang_field.setDisabled(True)
        self._ui.lang_list.setDisabled(True)

    def change_root_dir(self):
        self._model.dir = str(QFileDialog.getExistingDirectory(self._ui.directory_tool, "Select Directory"))
        self._controller.init_project()
        self._ui.directory_display.setText(self._model.dir)

    def fill_project_list(self, project_list):
        self._ui.project_list.clear()
        for project in project_list:
            self._ui.project_list.addItem(project)

    def fill_day_list(self, day_list):
        self._ui.day_list.clear()
        for info in day_list:
            self._ui.day_list.addItem(info)

    def fill_block_list(self, block_list):
        self._ui.block_list.clear()
        for info in block_list:
            self._ui.block_list.addItem(info)

    def fill_lang_list(self, lang_list):
        self._ui.lang_list.clear()
        for info in lang_list:
            self._ui.lang_list.addItem(info)

        self.enable_lang()

    def day_list_event(self):
        self._ui.delete_block_button.setDisabled(True)
        self._ui.edit_block_button.setDisabled(True)

        if not self._ui.day_list.selectedItems():
            return

        if not self.day_frame_active:
            self.enable_day()

        self._model.set_days(self._ui.day_list.currentRow())
        index = self._ui.day_list.currentRow()
        day = self._model.u_survey.days[index]
        self._model.u_day = day
        self._ui.day_field.setValue(day.day)
        self._ui.meta_field.setPlainText(day.meta)

        block_list = []
        for block in day.blocks:
            block_list.append(block.info())
        self.fill_block_list(block_list)

    def block_list_event(self):
        if not self._ui.block_list.selectedItems():
            return

        index = self._ui.block_list.currentRow()
        self._model.u_block = self._model.u_day.blocks[index]

        self._ui.edit_block_button.setEnabled(True)
        self._ui.delete_block_button.setEnabled(True)

    def edit_block(self):
        self._model.lang = self._model.default_language
        self._model.set_blocks(self._ui.block_list.currentRow())
        self.parent().setCurrentIndex(1)

    def activate_project_options(self):
        self._ui.load_project_button.setEnabled(True)
        self._ui.delete_project_button.setEnabled(True)

    def deactivate_project_options(self):
        self._ui.load_project_button.setDisabled(True)
        self._ui.delete_project_button.setDisabled(True)

    def load_project(self):
        index = self._ui.project_list.currentRow()
        self._model.dir = self._model.recent_projects[index]
        self._controller.init_project()

    def delete_project(self):
        index = self._ui.project_list.currentRow()
        self._ui.project_list.takeItem(index)
        del self._model.recent_projects[index]
        if len(self._model.recent_projects) == 0:
            self.deactivate_project_options()

    def save_meta(self):
        meta = self._ui.meta_field.toPlainText()
        self._model.save_day_meta(meta)
        self.update_info()

    def set_day(self):
        pass  # todo

    def update_info(self):
        lang = self._model.default_language
        days = []
        blocks = []
        for day in self._model.surveys[lang].days:
            days.append(day.info())

        for block in self._model.days[lang].blocks:
            blocks.append(block.info())

        self.fill_day_list(days)
        self.fill_block_list(blocks)
