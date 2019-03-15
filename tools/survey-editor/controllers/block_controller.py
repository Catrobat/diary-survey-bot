from PyQt5.QtCore import QObject, pyqtSlot

# The controller class performs any logic and sets data in the model.
from model.survey import Question


class BlockController(QObject):
    def __init__(self, model):
        super().__init__()
        self._model = model

    def add_question(self):
        for lang in self._model.languages:
            question = Question()
            survey = self._model.surveys[lang]
            day = self._model.days[lang]
            block = self._model.blocks[lang]

            question.set_survey(survey)
            question.set_day(day)
            question.set_block(block)

            self._model.blocks[lang].questions.append(question)

        block = self._model.blocks[self._model.default_language]
        questions = []
        for item in block.questions:
            questions.append(item.info())
        return questions

    def delete_question(self, index):
        for lang in self._model.languages:
            del self._model.blocks[lang].questions[index]

        self._model.update_surveys()

        block = self._model.blocks[self._model.default_language]
        questions = []
        for item in block.questions:
            questions.append(item.info())
        return questions
