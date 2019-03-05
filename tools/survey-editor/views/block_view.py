from PyQt5.QtWidgets import QWidget

from controllers.question_controller import QuestionController
from views.block_view_ui import Ui_Block
from views.question_view import QuestionView


# The view class should mainly contain code to handle events and trigger
# events in/from the user interface.
class BlockView(QWidget):
    def __init__(self, model, block_controller):
        super().__init__()

        self._model = model
        self._controller = block_controller
        self._ui = Ui_Block()
        self._ui.setupUi(self)
        self._view = None

        self._ui.back_to_days_button.clicked.connect(self.back_to_days)

    def back_to_days(self):
        self.parent().setCurrentIndex(0)

    def populate(self):
        q_controller = QuestionController(self._model)
        for i in range(len(self._model.languages)):
            if not self._ui.tabWidget.tabText(i) in self._model.languages:
                q_view = QuestionView(self._model, q_controller, self._model.languages[i])
                self._ui.tabWidget.addTab(q_view, self._model.languages[i])
                q_view.populate(self._model.languages[i])
