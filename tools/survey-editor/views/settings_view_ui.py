# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName("Settings")
        Settings.resize(1366, 768)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setBold(False)
        font.setWeight(50)
        Settings.setFont(font)
        self.gridLayout_4 = QtWidgets.QGridLayout(Settings)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame = QtWidgets.QFrame(Settings)
        self.frame.setMinimumSize(QtCore.QSize(320, 0))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 75))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.headline = QtWidgets.QLabel(self.frame)
        self.headline.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.headline.setFont(font)
        self.headline.setAlignment(QtCore.Qt.AlignCenter)
        self.headline.setObjectName("headline")
        self.gridLayout.addWidget(self.headline, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame, 0, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(Settings)
        self.frame_2.setMinimumSize(QtCore.QSize(320, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.frame_2.setFont(font)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.name_headline = QtWidgets.QLabel(self.frame_2)
        self.name_headline.setMinimumSize(QtCore.QSize(170, 0))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.name_headline.setFont(font)
        self.name_headline.setAlignment(QtCore.Qt.AlignCenter)
        self.name_headline.setObjectName("name_headline")
        self.horizontalLayout.addWidget(self.name_headline)
        self.name_field = QtWidgets.QLineEdit(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.name_field.setFont(font)
        self.name_field.setText("")
        self.name_field.setReadOnly(False)
        self.name_field.setPlaceholderText("")
        self.name_field.setObjectName("name_field")
        self.horizontalLayout.addWidget(self.name_field)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.language_headline = QtWidgets.QLabel(self.frame_2)
        self.language_headline.setMinimumSize(QtCore.QSize(170, 0))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.language_headline.setFont(font)
        self.language_headline.setAlignment(QtCore.Qt.AlignCenter)
        self.language_headline.setObjectName("language_headline")
        self.horizontalLayout_3.addWidget(self.language_headline)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.language_field = QtWidgets.QLineEdit(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.language_field.setFont(font)
        self.language_field.setText("")
        self.language_field.setReadOnly(True)
        self.language_field.setPlaceholderText("")
        self.language_field.setObjectName("language_field")
        self.horizontalLayout_2.addWidget(self.language_field)
        self.language_box = QtWidgets.QComboBox(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.language_box.setFont(font)
        self.language_box.setCurrentText("")
        self.language_box.setObjectName("language_box")
        self.horizontalLayout_2.addWidget(self.language_box)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.editor_headline = QtWidgets.QLabel(self.frame_2)
        self.editor_headline.setMinimumSize(QtCore.QSize(170, 0))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.editor_headline.setFont(font)
        self.editor_headline.setAlignment(QtCore.Qt.AlignCenter)
        self.editor_headline.setObjectName("editor_headline")
        self.horizontalLayout_4.addWidget(self.editor_headline)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.editor_field = QtWidgets.QLineEdit(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.editor_field.setFont(font)
        self.editor_field.setText("")
        self.editor_field.setReadOnly(True)
        self.editor_field.setPlaceholderText("")
        self.editor_field.setObjectName("editor_field")
        self.horizontalLayout_5.addWidget(self.editor_field)
        self.editor_box = QtWidgets.QComboBox(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.editor_box.setFont(font)
        self.editor_box.setObjectName("editor_box")
        self.editor_box.addItem("")
        self.editor_box.addItem("")
        self.horizontalLayout_5.addWidget(self.editor_box)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.custom_headline = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.custom_headline.setFont(font)
        self.custom_headline.setAlignment(QtCore.Qt.AlignCenter)
        self.custom_headline.setObjectName("custom_headline")
        self.verticalLayout.addWidget(self.custom_headline)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.custom_field = QtWidgets.QLineEdit(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.custom_field.setFont(font)
        self.custom_field.setText("")
        self.custom_field.setReadOnly(False)
        self.custom_field.setPlaceholderText("")
        self.custom_field.setObjectName("custom_field")
        self.horizontalLayout_6.addWidget(self.custom_field)
        self.custom_add_button = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.custom_add_button.setFont(font)
        self.custom_add_button.setObjectName("custom_add_button")
        self.horizontalLayout_6.addWidget(self.custom_add_button)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.custom_list = QtWidgets.QListWidget(self.frame_2)
        self.custom_list.setMaximumSize(QtCore.QSize(16777215, 250))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.custom_list.setFont(font)
        self.custom_list.setObjectName("custom_list")
        self.verticalLayout.addWidget(self.custom_list)
        self.custom_delete_button = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.custom_delete_button.setFont(font)
        self.custom_delete_button.setObjectName("custom_delete_button")
        self.verticalLayout.addWidget(self.custom_delete_button)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 2, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 2, 1, 1)
        self.save_button = QtWidgets.QPushButton(self.frame_2)
        self.save_button.setObjectName("save_button")
        self.gridLayout_2.addWidget(self.save_button, 3, 1, 1, 1)
        self.gridLayout_4.addWidget(self.frame_2, 2, 0, 1, 1)

        self.retranslateUi(Settings)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        _translate = QtCore.QCoreApplication.translate
        Settings.setWindowTitle(_translate("Settings", "Form"))
        self.headline.setText(_translate("Settings", "Settings"))
        self.name_headline.setText(_translate("Settings", "Project Name:"))
        self.language_headline.setText(_translate("Settings", "Default Language:"))
        self.editor_headline.setText(_translate("Settings", "Editor Mode:"))
        self.editor_box.setCurrentText(_translate("Settings", "Admin"))
        self.editor_box.setItemText(0, _translate("Settings", "Admin"))
        self.editor_box.setItemText(1, _translate("Settings", "Translator"))
        self.custom_headline.setText(_translate("Settings", "Custom Keyboards"))
        self.custom_add_button.setText(_translate("Settings", "add"))
        self.custom_delete_button.setText(_translate("Settings", "delete"))
        self.save_button.setText(_translate("Settings", "save and return"))


