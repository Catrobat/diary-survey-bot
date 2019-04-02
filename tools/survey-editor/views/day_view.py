"""
diary-survey-bot | survey-editor

Software-Design: Philipp Feldner
Documentation: https://github.com/Catrobat/diary-survey-bot

Qt version: 5.12.1
"""

from PyQt5.QtWidgets import QWidget, QFileDialog

from model.survey import Block, Day
from resources.languages import iso_639_choices
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
        self._ui.block_list.itemDoubleClicked.connect(self.edit_block)
        self._ui.project_list.itemSelectionChanged.connect(self.activate_project_options)
        self._ui.load_project_button.clicked.connect(self.load_project)
        self._ui.delete_project_button.clicked.connect(self.delete_project)
        self._ui.edit_block_button.clicked.connect(self.edit_block)
        self._ui.meta_save_button.clicked.connect(self.save_meta)
        self._ui.day_set_button.clicked.connect(self.set_day)
        self._ui.day_template_load_button.clicked.connect(self.load_day_template)
        self._ui.day_template_del_button.clicked.connect(self.delete_day_template)
        self._ui.day_template_store_button.clicked.connect(self.store_day_template)
        self._ui.new_block_button.clicked.connect(self.new_block)
        self._ui.block_list.model().rowsMoved.connect(self.reorder_block)
        self._ui.delete_block_button.clicked.connect(self.delete_block)
        self._ui.move_up_button.clicked.connect(self.move_up_day)
        self._ui.shift_up_button.clicked.connect(self.shift_up_day)
        self._ui.move_down_button.clicked.connect(self.move_down_day)
        self._ui.shift_down_button.clicked.connect(self.shift_down_day)
        self._ui.new_day_button.clicked.connect(self.new_day)
        self._ui.delete_day_button.clicked.connect(self.delete_day)
        self._ui.lang_add_button.clicked.connect(self.add_lang)
        self._ui.lang_delete_button.clicked.connect(self.delete_lang)

    def enable_days(self):
        self._ui.move_down_button.setEnabled(True)
        self._ui.move_up_button.setEnabled(True)
        self._ui.shift_down_button.setEnabled(True)
        self._ui.shift_up_button.setEnabled(True)
        self._ui.headline_days.setEnabled(True)
        self._ui.day_list.setEnabled(True)
        self._ui.new_day_button.setEnabled(True)
        self._ui.delete_day_button.setEnabled(True)

    def disable_days(self):
        self._ui.move_down_button.setDisabled(True)
        self._ui.move_up_button.setDisabled(True)
        self._ui.shift_down_button.setDisabled(True)
        self._ui.shift_up_button.setDisabled(True)
        self._ui.headline_days.setDisabled(True)
        self._ui.day_list.setDisabled(True)
        self._ui.new_day_button.setDisabled(True)
        self._ui.delete_day_button.setDisabled(True)

    def enable_day(self):
        self._ui.day_template_box.setEnabled(True)
        self._ui.day_template_field.setEnabled(True)
        self._ui.day_template_load_button.setEnabled(True)
        self._ui.day_template_store_button.setEnabled(True)
        self._ui.day_template_del_button.setEnabled(True)
        self._ui.meta_save_button.setEnabled(True)
        self._ui.headline_day.setEnabled(True)
        self._ui.label_day.setEnabled(True)
        self._ui.day_field.setEnabled(True)
        self._ui.day_set_button.setEnabled(True)
        self._ui.label_meta.setEnabled(True)
        self._ui.meta_field.setEnabled(True)
        self._ui.label_blocks.setEnabled(True)
        self._ui.block_list.setEnabled(True)
        self._ui.new_block_button.setEnabled(True)
        self._ui.edit_block_button.setEnabled(True)
        self._ui.delete_block_button.setEnabled(True)
        self.day_frame_active = True

    def disable_day(self):
        self._ui.day_template_box.setDisabled(True)
        self._ui.day_template_field.setDisabled(True)
        self._ui.day_template_load_button.setDisabled(True)
        self._ui.day_template_store_button.setDisabled(True)
        self._ui.day_template_del_button.setDisabled(True)
        self._ui.meta_save_button.setDisabled(True)
        self._ui.headline_day.setDisabled(True)
        self._ui.label_day.setDisabled(True)
        self._ui.day_field.setDisabled(True)
        self._ui.day_set_button.setDisabled(True)
        self._ui.label_meta.setDisabled(True)
        self._ui.meta_field.setDisabled(True)
        self._ui.label_blocks.setDisabled(True)
        self._ui.block_list.setDisabled(True)
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
        if not self._ui.day_list.selectedItems():
            return
        self._ui.delete_block_button.setDisabled(True)
        self._ui.edit_block_button.setDisabled(True)

        if not self._ui.day_list.selectedItems():
            return

        if not self.day_frame_active:
            self.enable_day()

        self._model.set_days(self._ui.day_list.currentRow())
        index = self._ui.day_list.currentRow()
        day = self._model.surveys[self._model.default_language].days[index]
        self._ui.day_field.setValue(day.day)
        self._ui.meta_field.setPlainText(day.meta)

        block_list = []
        for block in day.blocks:
            block_list.append(block.info())
        self.fill_block_list(block_list)
        self.fill_day_templates()

    def block_list_event(self):
        if not self._ui.block_list.selectedItems():
            return

        index = self._ui.block_list.currentRow()
        self._model.set_blocks(index)

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
        day = self._ui.day_field.value()
        if self._controller.set_day(day):
            self.update_info()
        self._model.update_surveys()

    def update_info(self):
        block_index = self._ui.block_list.currentRow()
        day_index = self._ui.day_list.currentRow()
        lang = self._model.default_language
        days = []
        blocks = []
        for day in self._model.surveys[lang].days:
            days.append(day.info())

        if self._model.days:
            for block in self._model.days[lang].blocks:
                blocks.append(block.info())

        self._ui.block_list.disconnect()
        self._ui.day_list.disconnect()
        self.fill_day_list(days)
        self.fill_block_list(blocks)
        day = self._ui.day_list.item(day_index)
        if self._model.days:
            block = self._ui.block_list.item(block_index)
            self._ui.block_list.setCurrentItem(block)
        self._ui.day_list.setCurrentItem(day)
        self._ui.day_list.itemSelectionChanged.connect(self.day_list_event)
        self._ui.block_list.itemSelectionChanged.connect(self.block_list_event)
        self._ui.block_list.itemDoubleClicked.connect(self.edit_block)

    def fill_day_templates(self):
        keys = self._model.get_day_template_keys()
        self._ui.day_template_box.clear()
        self._ui.day_template_box.addItems(keys)

    def store_day_template(self):
        key = self._ui.day_template_field.text()
        if key == "":
            return
        self._controller.build_day_template(key, self._model.days)
        self._ui.day_template_field.setText("")
        self.fill_day_templates()

    def load_day_template(self):
        key = self._ui.day_template_box.currentText()
        self._controller.load_day_template(key)
        self.update_info()
        self._model.update_surveys()

    def delete_day_template(self):
        key = self._ui.day_template_box.currentText()
        del self._model.day_templates[key]
        self.fill_day_templates()

    def new_block(self):
        for lang in self._model.languages:
            block = Block()
            block.set_day(self._model.days[lang])
            block.set_survey(self._model.surveys[lang])
            self._model.days[lang].add_block(block)
        self._model.update_surveys()
        self.update_info()

    def delete_block(self):
        if not self._ui.block_list.selectedItems():
            return
        index = self._ui.block_list.currentRow()
        for lang in self._model.languages:
            self._model.days[lang].blocks.pop(index)
        self._model.update_surveys()
        self.update_info()

    def reorder_block(self, p, old, end, q, new):
        for lang in self._model.languages:
            self._model.days[lang].blocks.insert(new, self._model.days[lang].blocks.pop(old))
        self._model.update_surveys()
        self.update_info()

    def move_up_day(self):
        if not self._ui.day_list.selectedItems():
            return
        index = self._ui.day_list.currentRow()
        direction = -1
        if self._controller.move_day(index, direction):
            days = []
            for day in self._model.surveys[self._model.default_language].days:
                days.append(day.info())
            self.fill_day_list(days)
            day = self._ui.day_list.item(index + direction)
            self._ui.day_list.setCurrentItem(day)

    def shift_up_day(self):
        if not self._ui.day_list.selectedItems():
            return
        index = self._ui.day_list.currentRow()
        direction = -1
        self._controller.shift_day(index, direction)
        self.update_info()

    def move_down_day(self):
        if not self._ui.day_list.selectedItems():
            return
        index = self._ui.day_list.currentRow()
        direction = 1
        if self._controller.move_day(index, direction):
            days = []
            for day in self._model.surveys[self._model.default_language].days:
                days.append(day.info())
            self.fill_day_list(days)
            day = self._ui.day_list.item(index + direction)
            self._ui.day_list.setCurrentItem(day)

    def shift_down_day(self):
        if not self._ui.day_list.selectedItems():
            return
        index = self._ui.day_list.currentRow()
        direction = 1
        self._controller.shift_day(index, direction)
        self.update_info()

    def new_day(self):
        index = 1
        if not self._model.surveys[self._model.default_language].days == []:
            index = self._model.surveys[self._model.default_language].days[-1].day + 1
        for lang in self._model.languages:
            day = Day()
            day.set_day(index)
            self._model.surveys[lang].add_day(day)
        self._model.update_surveys()
        self.update_info()

        max_index = 0
        if self._model.surveys[self._model.default_language].days:
            max_index = len(self._model.surveys[self._model.default_language].days) - 1
        item = self._ui.day_list.item(max_index)
        self._ui.day_list.setCurrentItem(item)

    def delete_day(self):
        if not self._ui.day_list.selectedItems():
            return
        index = self._ui.day_list.currentRow()
        for lang in self._model.languages:
            del self._model.surveys[lang].days[index]
        self.update_info()
        self._model.update_surveys()
        item = self._ui.day_list.item(index - 1)
        self._ui.day_list.setCurrentItem(item)

    def add_lang(self):
        lang = self._ui.lang_field.text()
        if lang not in iso_639_choices or lang in self._model.languages:
            # todo error handling
            return
        self._controller.add_lang(lang)
        self._ui.lang_list.addItem(lang + " -> " + iso_639_choices[lang])
        # 3 fix templates

        self._ui.day_list.clearSelection()
        self.disable_day()

    def delete_lang(self):
        if not self._ui.lang_list.selectedItems():
            return
        index = self._ui.lang_list.currentRow()
        lang = self._ui.lang_list.item(index).text()[:2]
        self._controller.delete_language(lang)
        self._ui.lang_list.takeItem(index)
        self.block_view.remove_tab(lang)
        self._ui.day_list.clearSelection()
        self.disable_day()


