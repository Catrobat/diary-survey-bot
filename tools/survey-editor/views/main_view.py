"""
diary-survey-bot | survey-editor

Software-Design: Philipp Feldner
Documentation: https://github.com/Catrobat/diary-survey-bot

Qt version: 5.12.1
"""

from PyQt5.QtWidgets import QMainWindow
from controllers.block_controller import BlockController
from controllers.day_controller import DayController
from controllers.settings_controller import SettingsController
from views.block_view import BlockView
from views.day_view import DayView
from views.main_view_ui import Ui_main_window


# The view class should mainly contain code to handle events and trigger
# events in/from the user interface.
# related .ui file in ../qt/mainwindow.ui
from views.settings_view import SettingsView


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
        self.settings_controller = SettingsController(self._model)

        self.day_view = DayView(self._model, self.day_controller)
        self.block_view = BlockView(self._model, self.block_controller)
        self.settings_view = SettingsView(self._model, self.settings_controller)

        self.block_view.day_view = self.day_view
        self.day_view.block_view = self.block_view

        self.day_controller._view = self.day_view
        self.block_controller._view = self.block_view

        self._ui.stackedWidget.addWidget(self.day_view)
        self._ui.stackedWidget.addWidget(self.block_view)
        self._ui.stackedWidget.addWidget(self.settings_view)

        self._ui.stackedWidget.currentChanged.connect(self.widget_change)

    def widget_change(self):
        index = self._ui.stackedWidget.currentIndex()
        if index == 1:
            self.block_view.populate()
        if index == 2:
            self.settings_view.populate()
        # todo add a way to switch between settings/block/day
