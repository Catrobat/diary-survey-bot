"""
diary-survey-bot | survey-editor

Software-Design: Philipp Feldner
Documentation: https://github.com/Catrobat/diary-survey-bot

Qt version: 5.12.1
"""

from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QMessageBox
from views.question_view_ui import Ui_question
from resources.settings import question_commands


# The view class should mainly contain code to handle events and trigger
# events in/from the user interface.
# related .ui file in ../qt/question.ui
class QuestionView(QWidget):
    def __init__(self, model, question_controller, language):
        super().__init__()

        self._lang = language
        self._model = model
        self._block_view = None

        self._controller = question_controller
        self._ui = Ui_question()
        self._ui.setupUi(self)

        commands = [command[0] for command in question_commands]
        for item in commands:
            self._ui.commands_combobox.addItem(item)

        self._ui.choice_list.model().rowsMoved.connect(lambda: self._controller.update_choice(self._ui.choice_list))
        self._ui.choice_add_button.clicked.connect(self.add_choice)
        self._ui.choice_delete_button.clicked.connect(self.delete_choice)
        self._ui.save_button.clicked.connect(self.save_data)
        self._ui.choice_list.itemSelectionChanged.connect(self.edit_choice)
        self._ui.choice_list.itemDoubleClicked.connect(self.clear_selection)
        self._ui.condition_add_button.clicked.connect(self.build_condition)
        self._ui.condition_delete_button.clicked.connect(self.delete_condition)
        self._ui.condition_rq_add_button.clicked.connect(self.add_condition_rq)
        self._ui.condition_rq_delete_button.clicked.connect(self.delete_condition_rq)
        self._ui.command_add_button.clicked.connect(self.add_command)
        self._ui.command_data_add_button.clicked.connect(self.build_command)
        self._ui.commands_delete_button.clicked.connect(self.delete_command)
        self._ui.choice_template_load_button.clicked.connect(self.load_choice_template)
        self._ui.choice_template_del_button.clicked.connect(self.delete_choice_template)
        self._ui.choice_template_store_button.clicked.connect(self.store_choice_template)
        self._ui.question_template_load_button.clicked.connect(self.load_question_template)
        self._ui.question_template_del_button.clicked.connect(self.delete_question_template)
        self._ui.question_template_store_button.clicked.connect(self.store_question_template)

    def populate(self):
        question = self._model.questions[self._lang]
        index = question.block.questions.index(question)
        self._ui.lang_info.setText(self._lang)
        self._ui.day_info.setText("Day: #" + str(question.day.day))
        self._ui.block_info.setText("Block: #" + str(question.day.blocks.index(question.block) + 1))

        self.fill_choices(question.choice)
        self.set_question_number(index + 1)
        self.fill_text(question.text)
        self.fill_meta(question.meta)
        self.fill_variable(question.variable)
        self.fill_commands()
        self.fill_condition()
        self.fill_all_conditions_list()
        self.fill_condition_required()
        self.fill_choice_templates()
        self.fill_question_templates()

        self._ui.keyword_field.setText("")
        self._ui.choice_template_field.setText("")
        self._ui.question_template_field.setText("")
        self._ui.choice_field.setPlainText("")
        self._ui.question_template_field.setText("")
        self._ui.data_name_field.setText("")

    def set_question_number(self, nr):
        self._ui.headline.setText("Question #" + str(nr))

    def fill_text(self, text):
        self._ui.text_field.setPlainText(text)

    def fill_meta(self, meta):
        self._ui.meta_field.setPlainText(meta)

    def fill_variable(self, variable):
        self._ui.variable_field.setText(variable)

    def add_choice(self):
        if not self._ui.choice_list.selectedItems():
            if self._ui.choice_field.toPlainText() != "":
                self._ui.choice_list.addItem(self._ui.choice_field.toPlainText())
                self._ui.choice_field.setPlainText("")
                self._controller.update_choice(self._ui.choice_list)
        else:
            if self._ui.choice_field.toPlainText() != "":
                index = self._ui.choice_list.currentRow()
                self._ui.choice_list.item(index).setText(self._ui.choice_field.toPlainText())
                self._ui.choice_field.setPlainText("")
                self._ui.choice_list.clearSelection()
                self._controller.update_choice(self._ui.choice_list)
        self.update_condition_choice_list()

    def delete_choice(self):
        if self._ui.choice_list.selectedItems():
            self._ui.choice_list.takeItem(self._ui.choice_list.currentRow())
            self._controller.update_choice(self._ui.choice_list)
            self._ui.choice_field.setPlainText("")
            self._ui.choice_list.clearSelection()
        self.update_condition_choice_list()

    def fill_choices(self, choices):
        self._ui.choice_list.clear()
        self._ui.condition_choice_list.clear()
        for choice in choices:
            self._ui.choice_list.addItem(choice[0])
        self.update_condition_choice_list()

    def build_condition(self):
        if not self._ui.condition_choice_list.selectedItems() or self._ui.keyword_field.text() == "":
            return

        keyword = self._ui.keyword_field.text()
        index = self._ui.condition_choice_list.currentRow()
        choice = self._ui.condition_choice_list.item(index).text()
        if not self._controller.build_condition(keyword, choice):
            return
        self.fill_condition()

    def delete_condition(self):
        if not self._ui.condition_list.selectedItems():
            return

        index = self._ui.condition_list.currentRow()
        choice = self._ui.condition_list.item(index, 0).text()
        key = self._ui.condition_list.item(index, 1).text()
        item = [choice, key]
        self._model.questions[self._model.lang].delete_condition(item)
        self._model.cleanup_condition(item)
        coordinates = self._model.get_current_coordinates()
        coordinates.append(item)
        self._model.conditions[self._model.lang].remove(coordinates)
        self._model.update_surveys()
        self.fill_condition()

    def fill_condition(self):
        conditions = self._model.questions[self._model.lang].condition
        self._ui.condition_list.setRowCount(0)

        for condition in conditions:
            size = self._ui.condition_list.rowCount()
            self._ui.condition_list.insertRow(size)
            self._ui.condition_list.setItem(size, 0, QTableWidgetItem(condition[0]))
            self._ui.condition_list.setItem(size, 1, QTableWidgetItem(condition[1]))

    def add_command(self):
        command = [self._ui.commands_combobox.currentText()]
        if command in self._model.questions[self._model.lang].commands:
            return
        for lang in self._model.languages:
            self._model.questions[lang].add_command(command)

        self._model.update_surveys()
        self.fill_commands()

    def build_command(self):
        if self._ui.data_name_field.text() == "":
            return
        data_name = self._ui.data_name_field.text()
        operation = self._ui.data_box.currentText()
        command = ["DATA", data_name, operation]

        if command in self._model.questions[self._model.lang].commands:
            return

        for lang in self._model.languages:
            self._model.questions[lang].add_command(command)

        self._model.update_surveys()
        self.fill_commands()

    def delete_command(self):
        if not self._ui.commands_list.selectedItems():
            return
        index = self._ui.commands_list.currentRow()
        text = self._ui.commands_list.item(index).text()
        command = text.replace("'", "").replace("[", "").replace("]", "").split(", ")
        for lang in self._model.languages:
            self._model.questions[lang].delete_command(command)

        self._model.update_surveys()
        self.fill_commands()

    def fill_commands(self):
        commands = self._model.questions[self._model.lang].commands
        self._ui.commands_list.clear()
        for command in commands:
            self._ui.commands_list.addItem(str(command))

    def add_condition_rq(self):
        if not self._ui.all_conditions_list.selectedItems():
            return

        index = self._ui.all_conditions_list.currentRow()
        choice = self._ui.all_conditions_list.item(index, 0).text()
        key = self._ui.all_conditions_list.item(index, 1).text()
        condition = [choice, key]
        self._model.questions[self._model.lang].add_condition_rq(condition)
        self.fill_condition_required()

    def delete_condition_rq(self):
        if not self._ui.rq_conditions_list.selectedItems():
            return

        index = self._ui.rq_conditions_list.currentRow()
        choice = self._ui.rq_conditions_list.item(index, 0)
        key = self._ui.rq_conditions_list.item(index, 1)
        condition = [choice, key]
        self._model.questions[self._model.lang].delete_condition_rq(condition)
        self.fill_condition_required()

    def fill_all_conditions_list(self):
        all_conditions = self._controller.calc_all_conditions()
        self._ui.all_conditions_list.setRowCount(0)
        for condition in all_conditions:
            size = self._ui.all_conditions_list.rowCount()
            self._ui.all_conditions_list.insertRow(size)
            self._ui.all_conditions_list.setItem(size, 0, QTableWidgetItem(condition[0]))
            self._ui.all_conditions_list.setItem(size, 1, QTableWidgetItem(condition[1]))

    def fill_condition_required(self):
        conditions = self._model.questions[self._model.lang].condition_required
        self._ui.rq_conditions_list.setRowCount(0)
        for condition in conditions:
            size = self._ui.rq_conditions_list.rowCount()
            self._ui.rq_conditions_list.insertRow(size)
            self._ui.rq_conditions_list.setItem(size, 0, QTableWidgetItem(condition[0]))
            self._ui.rq_conditions_list.setItem(size, 1, QTableWidgetItem(condition[1]))

    def save_data(self):
        variable = self._ui.variable_field.text()
        meta = self._ui.meta_field.toPlainText()
        text = self._ui.text_field.toPlainText()
        self._model.set_question_metavar(meta, variable)
        self._controller.update_question(text)
        self._model.update_surveys()
        if self._model.lang == self._model.default_language:
            questions = []
            for item in self._model.blocks[self._model.lang].questions:
                questions.append(item.info())
            self._block_view.fill_question_list(questions)

    def edit_choice(self):
        if not self._ui.choice_list.selectedItems():
            return
        index = self._ui.choice_list.currentRow()
        self._ui.choice_field.setPlainText(self._ui.choice_list.item(index).text())
        self.update_condition_choice_list()

    def clear_selection(self):
        self._ui.choice_field.setPlainText("")
        self._ui.choice_list.clearSelection()

    def update_condition_choice_list(self):
        self._ui.condition_choice_list.clear()
        for i in range(self._ui.choice_list.count()):
            self._ui.condition_choice_list.addItem(self._ui.choice_list.item(i).text())

    def fill_choice_templates(self):
        keys = self._model.get_choice_template_keys()
        self._ui.choice_template_box.clear()
        self._ui.choice_template_box.addItems(keys)

    def store_choice_template(self):
        key = self._ui.choice_template_field.text()
        if key == "":
            return
        if key in self._model.choice_templates:
            message = "This key is already in use. Do you want to overwrite it?"
            box = QMessageBox()
            reply = QMessageBox.question(box, 'Error', message, QMessageBox.Yes | QMessageBox.Cancel)
            if reply == QMessageBox.Cancel:
                return
        self._model.add_choice_template(key, self._model.questions[self._model.lang].choice)
        self._ui.choice_template_field.setText("")
        self.fill_choice_templates()

    def load_choice_template(self):
        key = self._ui.choice_template_box.currentText()
        choice = self._model.choice_templates[key]
        self._model.questions[self._model.lang].choice = choice
        self._model.update_surveys()
        self.fill_choices(choice)

    def delete_choice_template(self):
        key = self._ui.choice_template_box.currentText()
        del self._model.choice_templates[key]
        self.fill_choice_templates()

    def fill_question_templates(self):
        keys = self._model.get_question_template_keys()
        self._ui.question_template_box.clear()
        self._ui.question_template_box.addItems(keys)

    def store_question_template(self):
        key = self._ui.question_template_field.text()
        if key == "":
            return
        if key in self._model.question_templates:
            message = "This key is already in use. Do you want to overwrite it?"
            box = QMessageBox()
            reply = QMessageBox.question(box, 'Error', message, QMessageBox.Yes | QMessageBox.Cancel)
            if reply == QMessageBox.Cancel:
                return
        self._controller.build_question_template(key, self._model.questions)
        self._ui.question_template_field.setText("")
        self.fill_question_templates()

    def load_question_template(self):
        key = self._ui.question_template_box.currentText()
        if not self._controller.load_question_template(key):
            return
        self.populate()
        questions = []
        block = self._model.blocks[self._model.default_language]
        for item in block.questions:
            questions.append(item.info())
        self._block_view.fill_question_list(questions)

    def delete_question_template(self):
        key = self._ui.question_template_box.currentText()
        del self._model.question_templates[key]
        self.fill_question_templates()
