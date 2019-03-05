from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtCore import pyqtSlot

from controllers.block_controller import BlockController
from controllers.day_controller import DayController
from views.block_view import BlockView
from views.day_view import DayView
from views.main_view_ui import Ui_main_window


# The view class should mainly contain code to handle events and trigger
# events in/from the user interface.
class MainView(QMainWindow):
    def __init__(self, model, main_controller):
        super().__init__()

        self._model = model
        self._model.main_view = self
        self._controller = main_controller
        self._ui = Ui_main_window()
        self._ui.setupUi(self)

        self.day_controller = DayController(self._model)
        self.block_controller = BlockController(self._model)

        self.day_view = DayView(self._model, self.day_controller)
        self.block_view = BlockView(self._model, self.block_controller)

        self.day_controller._view = self.day_view
        self.block_controller._view = self.block_view

        self._ui.stackedWidget.addWidget(self.day_view)
        self._ui.stackedWidget.addWidget(self.block_view)
