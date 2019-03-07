from PyQt5.QtCore import QObject, pyqtSlot


# The controller class performs any logic and sets data in the model.


class QuestionController(QObject):
    def __init__(self, model):
        super().__init__()
        self._model = model

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


