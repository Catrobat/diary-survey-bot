from PyQt5.QtCore import QObject, pyqtSlot


# The controller class performs any logic and sets data in the model.


class QuestionController(QObject):
    def __init__(self, model):
        super().__init__()
        self._model = model

    def update_choice(self, choices):
        choice = []
        for i in range(choices.count()):
            choice.append(choices.item(i).text())
            # print(choice) todo
