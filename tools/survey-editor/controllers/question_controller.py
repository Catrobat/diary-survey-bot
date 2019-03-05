from PyQt5.QtCore import QObject, pyqtSlot

# The controller class performs any logic and sets data in the model.


class QuestionController(QObject):
    def __init__(self, model):
        super().__init__()
        self._model = model
