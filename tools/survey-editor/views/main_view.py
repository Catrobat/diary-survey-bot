from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtCore import pyqtSlot

from controllers.block_controller import BlockController
from controllers.question_controller import QuestionController
from views.block_view import BlockView
from views.main_view_ui import Ui_main_window
from views.question_view import QuestionView
from model.survey import Question


# The view class should mainly contain code to handle events and trigger
# events in/from the user interface.
class MainView(QMainWindow):
    def __init__(self, model, main_controller):
        super().__init__()

        self._model = model
        self._controller = main_controller
        self._ui = Ui_main_window()
        self._ui.setupUi(self)

        self.day_frame_active = False

        self.block_view = None

        # connect widgets to controller
        # self._ui.pushButton_reset.clicked.connect(lambda: self._main_controller.change_amount(0))

        # self._ui.placeholder_1.clicked.connect(self.change_view)
        # question_controller = QuestionController(Question)
        # self.question_view = QuestionView(Question, question_controller)

        # Register connections here
        self._ui.directory_tool.clicked.connect(self.change_root_dir)
        self._ui.day_list.itemSelectionChanged.connect(self.day_list_event)
        self._ui.block_list.itemSelectionChanged.connect(self.block_list_event)

        self._ui.edit_block_button.clicked.connect(self.edit_block)

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
        # Todo: remove/change
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

        index = self._ui.block_list.currentRow()
        self._model.u_block = self._model.u_day.blocks[index]

        self._ui.edit_block_button.setEnabled(True)
        self._ui.delete_block_button.setEnabled(True)

    def edit_block(self):
        self.block_view = BlockView(self._model, BlockController(self._model))
        self.setCentralWidget(self.block_view)
        self.block_view.show()
