import json
import re
import os

from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtCore import pyqtSlot

from controllers.question_controller import QuestionController
from views.main_view_ui import Ui_main_window
from views.question_view import QuestionView
from model.survey import Question

# The view class should contain the minimal code required to connect to the signals coming from
# the widgets in your layout.View events can call and pass basic information to a method in the view
# class and onto a method in a controller class, where any logic should be.


class MainView(QMainWindow):
    def __init__(self, model, main_controller):
        super().__init__()

        self._model = model
        self._controller = main_controller
        self._ui = Ui_main_window()
        self._ui.setupUi(self)

        self.day_frame_active = False

        # connect widgets to controller
        # self._ui.spinBox_amount.valueChanged.connect(self._main_controller.change_amount)
        # self._ui.pushButton_reset.clicked.connect(lambda: self._main_controller.change_amount(0))

        self._ui.placeholder_1.clicked.connect(self.change_view)
        question_controller = QuestionController(Question)
        self.question_view = QuestionView(Question, question_controller)

        # Register connections here
        self._ui.directory_tool.clicked.connect(self.change_root_dir)
        self._ui.day_list.itemSelectionChanged.connect(self.day_list_event)
        self._ui.block_list.itemSelectionChanged.connect(self.block_list_event)

        # listen for model event signals
        # self._model.amount_changed.connect(self.on_amount_changed)
        # self._model.even_odd_changed.connect(self.on_even_odd_changed)
        # self._model.enable_reset_changed.connect(self.on_enable_reset_changed)

        # set a default value
        # self._main_controller.change_amount(42)

    # @pyqtSlot(int)
    # def on_amount_changed(self, value):
    #     self._ui.spinBox_amount.setValue(value)
    #
    # @pyqtSlot(str)
    # def on_even_odd_changed(self, value):
    #     self._ui.label_even_odd.setText(value)
    #
    # @pyqtSlot(bool)
    # def on_enable_reset_changed(self, value):
    #     self._ui.pushButton_reset.setEnabled(value)

    def enable_day(self):
        self._ui.headline_day.setEnabled(True)
        self._ui.label_day.setEnabled(True)
        self._ui.day_field.setEnabled(True)
        self._ui.label_meta.setEnabled(True)
        self._ui.meta_field.setEnabled(True)
        self._ui.label_blocks.setEnabled(True)
        self._ui.block_list.setEnabled(True)
        self._ui.new_block_button.setEnabled(True)
        self.day_frame_active = True

    def disable_day(self):
        self._ui.headline_day.setDisabled(True)
        self._ui.label_day.setDisabled(True)
        self._ui.day_field.setDisabled(True)
        self._ui.label_meta.setDisabled(True)
        self._ui.meta_field.setDisabled(True)
        self._ui.label_blocks.setDisabled(True)
        self._ui.block_list.setEnabled(True)
        self._ui.new_block_button.setDisabled(True)
        self._ui.edit_block_button.setDisabled(True)
        self._ui.delete_block_button.setDisabled(True)
        self.day_frame_active = False

    def change_view(self):
        print("hello")
        self.setCentralWidget(self.question_view)
        self.question_view.show()

    def change_root_dir(self):
        self._model.dir = str(QFileDialog.getExistingDirectory(self._ui.directory_tool, "Select Directory"))
        self._controller.init_project()

    def fill_day_list(self, day_list):
        for info in day_list:
            self._ui.day_list.addItem(info)

    def fill_block_list(self, block_list):
        self._ui.block_list.clear()
        for info in block_list:
            self._ui.block_list.addItem(info)

    def day_list_event(self):
        self._ui.delete_block_button.setDisabled(True)
        self._ui.edit_block_button.setDisabled(True)

        if not self._ui.day_list.selectedItems():
            return

        if not self.day_frame_active:
            self.enable_day()

        index = self._ui.day_list.currentRow()
        day = self._model.u_survey.days[index]
        self._model.u_day = day
        self._ui.day_field.setValue(day.day)
        self._ui.meta_field.setPlainText(day.meta)

        block_list = []
        for block in day.blocks:
            block_list.append(block.info())
        self.fill_block_list(block_list)

    def block_list_event(self):
        if not self._ui.block_list.selectedItems():
            return

        self._ui.edit_block_button.setEnabled(True)
        self._ui.delete_block_button.setEnabled(True)
