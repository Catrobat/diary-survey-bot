from PyQt5.QtCore import QObject, pyqtSlot

# The controller class performs any logic and sets data in the model.
from model.survey import Question


class BlockController(QObject):
    def __init__(self, model):
        super().__init__()
        self._model = model
        self._view = None

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
        print(self._model.get_current_coordinates())
        for lang in self._model.languages:
            del self._model.blocks[lang].questions[index]

        self._model.update_surveys()

        block = self._model.blocks[self._model.default_language]
        questions = []
        for item in block.questions:
            questions.append(item.info())
        return questions

    def set_time(self, time):
        for lang in self._model.languages:
            self._model.blocks[lang].set_time(time)

        self._model.update_surveys()

    def reorder(self, question_list):
        order = []
        for i in range(question_list.count()):
            order.append(int(question_list.item(i).text().split(":")[0].replace("#", "")) - 1)

        for lang in self._model.languages:
            self._model.blocks[lang].questions = [self._model.blocks[lang].questions[i] for i in order]

        self._model.update_surveys()
        lang = self._model.default_language
        info = []
        for item in self._model.blocks[lang].questions:
            info.append(item.info())

        self._view.fill_question_list(info)

    def add_settings(self, item):
        for lang in self._model.languages:
            self._model.blocks[lang].add_settings([item])
        self._model.update_surveys()

    def delete_settings(self, item):
        for lang in self._model.languages:
            self._model.blocks[lang].delete_settings([item])
        self._model.update_surveys()
