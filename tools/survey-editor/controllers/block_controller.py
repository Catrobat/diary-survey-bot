"""
diary-survey-bot | survey-editor

Software-Design: Philipp Feldner
Documentation: https://github.com/Catrobat/diary-survey-bot

Qt version: 5.12.1
"""

from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QMessageBox
from model.survey import Question


# The controller class performs any logic and sets data in the model.
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
        if item == "MANDATORY":
            message = "Do not forget to add the command \"Continue automatic survey\" to the last mandatory " \
                      "question of this block. Otherwise the survey will not continue!"
            box = QMessageBox()
            QMessageBox.question(box, 'Warning!', message, QMessageBox.Ok)
        for lang in self._model.languages:
            self._model.blocks[lang].add_settings([item])
        self._model.update_surveys()

    def delete_settings(self, item):
        for lang in self._model.languages:
            self._model.blocks[lang].delete_settings([item])
        self._model.update_surveys()

    def build_block_template(self, key, blocks):
        template = {}
        for lang in blocks:
            template[lang] = blocks[lang].get_object()
        self._model.add_block_template(key, template)

    def load_block_template(self, key):
        template = self._model.block_templates[key]
        try:
            for lang in template:
                self._model.blocks[lang].set_meta(template[lang]["meta"])
                self._model.blocks[lang].set_settings(template[lang]["settings"])
                self._model.blocks[lang].questions = []
                for q in template[lang]["questions"]:
                    question = Question()
                    question.set_text(q["text"])
                    question.set_choice(q["choice"])
                    question.set_condition_required(q["condition_required"])
                    question.set_condition([])
                    question.set_commands(q["commands"])
                    question.set_meta(q["meta"])
                    question.set_variable(q["variable"])
                    question.set_block(self._model.blocks[lang])
                    question.set_day(self._model.days[lang])
                    question.set_survey(self._model.surveys[lang])
                    self._model.blocks[lang].add_question(question)
        except KeyError:
            message = "This template is corrupted!"
            box = QMessageBox()
            QMessageBox.question(box, 'Error', message, QMessageBox.Ok)
            return False
        return True
