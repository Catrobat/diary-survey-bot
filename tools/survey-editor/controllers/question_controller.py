from PyQt5.QtCore import QObject, pyqtSlot


# The controller class performs any logic and sets data in the model.


class QuestionController(QObject):
    def __init__(self, model):
        super().__init__()
        self._model = model
        self._view = None

    def update_choice(self, choices):
        choice = []
        lang = self._model.lang
        question = self._model.questions[lang]
        for i in range(choices.count()):
            choice.append([choices.item(i).text()])
        question.set_choice(choice)
        self._model.update_surveys()

    def update_question(self, text):
        lang = self._model.lang
        question = self._model.questions[lang]
        question.set_text(text)

    def build_condition(self, keyword, choice):
        condition = [choice, keyword]
        lang = self._model.lang
        if condition in self._model.questions[lang].condition:
            return False

        coordinates = self._model.get_current_coordinates()
        coordinates.append(condition)
        self._model.insert_condition_coordinates(coordinates)

        self._model.questions[lang].add_condition(condition)
        self._model.update_surveys()
        return True

    def calc_all_conditions(self):
        relevant_conditions = []
        coordinates = self._model.get_current_coordinates()

        conditions = self._model.conditions[self._model.lang]
        for item in conditions:
            if item[0] > coordinates[0] or \
              (item[0] == coordinates[0] and item[1] > coordinates[1]) or \
              (item[0] == coordinates[0] and item[1] == coordinates[1]) and item[2] >= coordinates[2]:
                break
            relevant_conditions.append(item[3])
        print(relevant_conditions)
        return relevant_conditions
