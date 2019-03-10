from PyQt5.QtWidgets import QWidget
from views.template_view_ui import Ui_Template


# The view class should mainly contain code to handle events and trigger
# events in/from the user interface.
class TemplateView(QWidget):
    def __init__(self, model, template_controller, language):
        super().__init__()

        self._lang = language
        self._model = model

        self._controller = template_controller
        self._ui = Ui_Template()
        self._ui.setupUi(self)
