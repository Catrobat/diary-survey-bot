from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSlot
from views.question_view_ui import Ui_question


# The view class should mainly contain code to handle events and trigger
# events in/from the user interface.
class QuestionView(QWidget):
    def __init__(self, model, question_controller):
        super().__init__()

        self._model = model
        self._question_controller = question_controller
        self._ui = Ui_question()
        self._ui.setupUi(self)
