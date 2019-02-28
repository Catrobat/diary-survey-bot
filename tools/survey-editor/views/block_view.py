from views.block_view_ui import Ui_Block
from views.question_view import QuestionView
from model.survey import Question


class BlockView:
    def __init__(self, model, block_controller):
        super().__init__()

        self._model = model
        self._controller = block_controller
        self._ui = Ui_Block()
        self._ui.setupUi(self)
