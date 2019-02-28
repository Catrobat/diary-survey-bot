import re
import os

from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtCore import pyqtSlot

from controllers.question_controller import QuestionController
from views.main_view_ui import Ui_main_window
from views.question_view import QuestionView
from model.survey import Question


class MainView(QMainWindow):
    def __init__(self, model, main_controller):
        super().__init__()

        self._model = model
        self._controller = main_controller
        self._ui = Ui_main_window()
        self._ui.setupUi(self)

        # connect widgets to controller
        #self._ui.spinBox_amount.valueChanged.connect(self._main_controller.change_amount)
        #self._ui.pushButton_reset.clicked.connect(lambda: self._main_controller.change_amount(0))

        self._ui.placeholder_1.clicked.connect(self.change_view)
        question_controller = QuestionController(Question)

        self.question_view = QuestionView(Question, question_controller)
        self._ui.toolButton.clicked.connect(self.init_project)
        self._ui.listWidget.clicked.connect(self.test)

        # listen for model event signals
        # self._model.amount_changed.connect(self.on_amount_changed)
        # self._model.even_odd_changed.connect(self.on_even_odd_changed)
        # self._model.enable_reset_changed.connect(self.on_enable_reset_changed)

        # set a default value
        #self._main_controller.change_amount(42)

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

    @pyqtSlot(bool)
    def change_view(self):
        print("hello")
        self.setCentralWidget(self.question_view)
        self.question_view.show()

    def init_project(self):
        rootdir = str(QFileDialog.getExistingDirectory(self._ui.widget, "Select Directory"))
        print("working directory set to: " + rootdir)
        self._model.dir = rootdir

        regex = re.compile('(question_set_..\.json)')

        for root, dirs, files in os.walk(rootdir):
            for file in files:
                if regex.match(file):
                    self._ui.listWidget.addItem(file)

    def test(self):
        print(self._ui.listWidget.currentItem().text())




