from PyQt5.QtWidgets import QWidget
from views.question_view_ui import Ui_question


# The view class should mainly contain code to handle events and trigger
# events in/from the user interface.
class QuestionView(QWidget):
    def __init__(self, model, question_controller, language):
        super().__init__()

        self._lang = language
        self._model = model
        self._block_view = None

        self._controller = question_controller
        self._ui = Ui_question()
        self._ui.setupUi(self)

        self._ui.choice_list.model().rowsMoved.connect(lambda: self._controller.update_choice(self._ui.choice_list))
        self._ui.choice_add_button.clicked.connect(self.add_choice)
        self._ui.choice_delete_button.clicked.connect(self.delete_choice)
        self._ui.save_button.clicked.connect(self.save_data)
        self._ui.choice_list.itemSelectionChanged.connect(self.edit_choice)
        self._ui.choice_list.itemDoubleClicked.connect(self.clear_selection)

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
        self.fill_commands(question.commands)
        self.fill_condition(question.condition)
        self.fill_condition_required(question.condition_required)

        # Todo
        # Commands
        # Conditions
        # Conditions required
        # ...

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

    def delete_choice(self):
        if self._ui.choice_list.selectedItems():
            self._ui.choice_list.takeItem(self._ui.choice_list.currentRow())
            self._controller.update_choice(self._ui.choice_list)
            self._ui.choice_field.setPlainText("")
            self._ui.choice_list.clearSelection()

    def fill_choices(self, choices):
        self._ui.choice_list.clear()
        for choice in choices:
            self._ui.choice_list.addItem(choice[0])

    def add_condition(self, condition):
        self._ui.choice_list.addItem(condition)

    def delete_condition(self):
        self._ui.choice_list.takeItem(self._ui.choice_list.currentIndex())

    def fill_condition(self, conditions):
        for condition in conditions:
            self._ui.condition_list.addItem(condition)

    def add_command(self, command):
        self._ui.commands_list.addItem(command)

    def delete_command(self):
        self._ui.commands_list.takeItem(self._ui.commands_list.currentIndex())

    def fill_commands(self, commands):
        self._ui.commands_list.clear()
        for command in commands:
            self._ui.commands_list.addItem(command)

    def fill_all_conditions_list(self, all_conditions):
        self._ui.all_conditions_list.clear()
        for condition in all_conditions:
            self._ui.all_conditions_list.addItem(condition)

    def fill_condition_required(self, conditions):
        self._ui.rq_conditions_list.clear()
        for condition in conditions:
            self._ui.rq_conditions_list.addItem(condition)

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

    def clear_selection(self):
        self._ui.choice_field.setPlainText("")
        self._ui.choice_list.clearSelection()
