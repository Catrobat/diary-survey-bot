import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


def app():
    my_app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle("Test")
    w.show()
    sys.exit(my_app.exec_())

app()