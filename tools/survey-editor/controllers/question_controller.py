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
        # Todo add to datastructure that for finding rq_conditions
        condition = [choice, keyword]
        lang = self._model.lang
        if condition in self._model.questions[lang].condition:
            return False
        self._model.questions[lang].add_condition(condition)
        self._model.update_surveys()
        return True



