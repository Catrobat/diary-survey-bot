# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'day.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Day(object):
    def setupUi(self, Day):
        Day.setObjectName("Day")
        Day.resize(1366, 768)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        Day.setFont(font)
        self.gridLayout_5 = QtWidgets.QGridLayout(Day)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.title_frame = QtWidgets.QFrame(Day)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.title_frame.setFont(font)
        self.title_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.title_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title_frame.setObjectName("title_frame")
        self.gridLayout = QtWidgets.QGridLayout(self.title_frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.title_frame)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.title_frame, 0, 0, 1, 3)
        self.settings_frame = QtWidgets.QFrame(Day)
        self.settings_frame.setMinimumSize(QtCore.QSize(0, 0))
        self.settings_frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.settings_frame.setFont(font)
        self.settings_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.settings_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.settings_frame.setObjectName("settings_frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.settings_frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.settings_button = QtWidgets.QPushButton(self.settings_frame)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.settings_button.setFont(font)
        self.settings_button.setObjectName("settings_button")
        self.gridLayout_3.addWidget(self.settings_button, 7, 0, 1, 1)
        self.lang_list = QtWidgets.QListWidget(self.settings_frame)
        self.lang_list.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.lang_list.setFont(font)
        self.lang_list.setObjectName("lang_list")
        self.gridLayout_3.addWidget(self.lang_list, 12, 0, 1, 1)
        self.recent_projects_headline = QtWidgets.QLabel(self.settings_frame)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.recent_projects_headline.setFont(font)
        self.recent_projects_headline.setAlignment(QtCore.Qt.AlignCenter)
        self.recent_projects_headline.setObjectName("recent_projects_headline")
        self.gridLayout_3.addWidget(self.recent_projects_headline, 3, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.settings_frame)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.line_3.setFont(font)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_3.addWidget(self.line_3, 1, 0, 1, 1)
        self.headline_languages = QtWidgets.QLabel(self.settings_frame)
        self.headline_languages.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.headline_languages.setFont(font)
        self.headline_languages.setAlignment(QtCore.Qt.AlignCenter)
        self.headline_languages.setObjectName("headline_languages")
        self.gridLayout_3.addWidget(self.headline_languages, 10, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.iso_label = QtWidgets.QLabel(self.settings_frame)
        self.iso_label.setEnabled(False)
        self.iso_label.setMinimumSize(QtCore.QSize(6, 0))
        self.iso_label.setMaximumSize(QtCore.QSize(55, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.iso_label.setFont(font)
        self.iso_label.setObjectName("iso_label")
        self.horizontalLayout_7.addWidget(self.iso_label)
        self.lang_field = QtWidgets.QLineEdit(self.settings_frame)
        self.lang_field.setEnabled(False)
        self.lang_field.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.lang_field.setFont(font)
        self.lang_field.setMaxLength(2)
        self.lang_field.setObjectName("lang_field")
        self.horizontalLayout_7.addWidget(self.lang_field)
        self.lang_add_button = QtWidgets.QPushButton(self.settings_frame)
        self.lang_add_button.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.lang_add_button.setFont(font)
        self.lang_add_button.setObjectName("lang_add_button")
        self.horizontalLayout_7.addWidget(self.lang_add_button)
        self.lang_delete_button = QtWidgets.QPushButton(self.settings_frame)
        self.lang_delete_button.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.lang_delete_button.setFont(font)
        self.lang_delete_button.setObjectName("lang_delete_button")
        self.horizontalLayout_7.addWidget(self.lang_delete_button)
        self.gridLayout_3.addLayout(self.horizontalLayout_7, 13, 0, 1, 1)
        self.templates_button = QtWidgets.QPushButton(self.settings_frame)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.templates_button.setFont(font)
        self.templates_button.setObjectName("templates_button")
        self.gridLayout_3.addWidget(self.templates_button, 8, 0, 1, 1)
        self.healdline_project = QtWidgets.QLabel(self.settings_frame)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.healdline_project.setFont(font)
        self.healdline_project.setAlignment(QtCore.Qt.AlignCenter)
        self.healdline_project.setObjectName("healdline_project")
        self.gridLayout_3.addWidget(self.healdline_project, 0, 0, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.settings_frame)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.line_4.setFont(font)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_3.addWidget(self.line_4, 11, 0, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.settings_frame)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.line_5.setFont(font)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout_3.addWidget(self.line_5, 6, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.load_project_button = QtWidgets.QPushButton(self.settings_frame)
        self.load_project_button.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.load_project_button.setFont(font)
        self.load_project_button.setObjectName("load_project_button")
        self.horizontalLayout_8.addWidget(self.load_project_button)
        self.delete_project_button = QtWidgets.QPushButton(self.settings_frame)
        self.delete_project_button.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.delete_project_button.setFont(font)
        self.delete_project_button.setObjectName("delete_project_button")
        self.horizontalLayout_8.addWidget(self.delete_project_button)
        self.gridLayout_3.addLayout(self.horizontalLayout_8, 5, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.directory_display = QtWidgets.QLineEdit(self.settings_frame)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.directory_display.setFont(font)
        self.directory_display.setReadOnly(True)
        self.directory_display.setObjectName("directory_display")
        self.horizontalLayout.addWidget(self.directory_display)
        self.directory_tool = QtWidgets.QToolButton(self.settings_frame)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.directory_tool.setFont(font)
        self.directory_tool.setObjectName("directory_tool")
        self.horizontalLayout.addWidget(self.directory_tool)
        self.gridLayout_3.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.line_6 = QtWidgets.QFrame(self.settings_frame)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.line_6.setFont(font)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout_3.addWidget(self.line_6, 9, 0, 1, 1)
        self.project_list = QtWidgets.QListWidget(self.settings_frame)
        self.project_list.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.project_list.setFont(font)
        self.project_list.setObjectName("project_list")
        self.gridLayout_3.addWidget(self.project_list, 4, 0, 1, 1)
        self.gridLayout_5.addWidget(self.settings_frame, 1, 0, 1, 1)
        self.days_frame = QtWidgets.QFrame(Day)
        self.days_frame.setMinimumSize(QtCore.QSize(0, 0))
        self.days_frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.days_frame.setFont(font)
        self.days_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.days_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.days_frame.setObjectName("days_frame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.days_frame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.headline_days = QtWidgets.QLabel(self.days_frame)
        self.headline_days.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.headline_days.setFont(font)
        self.headline_days.setAlignment(QtCore.Qt.AlignCenter)
        self.headline_days.setObjectName("headline_days")
        self.gridLayout_4.addWidget(self.headline_days, 0, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.days_frame)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.line_2.setFont(font)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_4.addWidget(self.line_2, 1, 0, 1, 1)
        self.day_list = QtWidgets.QListWidget(self.days_frame)
        self.day_list.setEnabled(False)
        self.day_list.setMaximumSize(QtCore.QSize(1677215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.day_list.setFont(font)
        self.day_list.setObjectName("day_list")
        self.gridLayout_4.addWidget(self.day_list, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.new_day_button = QtWidgets.QPushButton(self.days_frame)
        self.new_day_button.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.new_day_button.setFont(font)
        self.new_day_button.setObjectName("new_day_button")
        self.horizontalLayout_2.addWidget(self.new_day_button)
        self.delete_day_button = QtWidgets.QPushButton(self.days_frame)
        self.delete_day_button.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.delete_day_button.setFont(font)
        self.delete_day_button.setObjectName("delete_day_button")
        self.horizontalLayout_2.addWidget(self.delete_day_button)
        self.gridLayout_4.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        self.gridLayout_5.addWidget(self.days_frame, 1, 1, 1, 1)
        self.day_frame = QtWidgets.QFrame(Day)
        self.day_frame.setMinimumSize(QtCore.QSize(0, 0))
        self.day_frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.day_frame.setFont(font)
        self.day_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.day_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.day_frame.setObjectName("day_frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.day_frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.headline_day = QtWidgets.QLabel(self.day_frame)
        self.headline_day.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.headline_day.setFont(font)
        self.headline_day.setAlignment(QtCore.Qt.AlignCenter)
        self.headline_day.setObjectName("headline_day")
        self.verticalLayout_3.addWidget(self.headline_day)
        self.line = QtWidgets.QFrame(self.day_frame)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.line.setFont(font)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_day = QtWidgets.QLabel(self.day_frame)
        self.label_day.setEnabled(False)
        self.label_day.setMinimumSize(QtCore.QSize(50, 0))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.label_day.setFont(font)
        self.label_day.setObjectName("label_day")
        self.horizontalLayout_4.addWidget(self.label_day)
        self.day_field = QtWidgets.QSpinBox(self.day_frame)
        self.day_field.setEnabled(False)
        self.day_field.setMaximumSize(QtCore.QSize(55, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.day_field.setFont(font)
        self.day_field.setObjectName("day_field")
        self.horizontalLayout_4.addWidget(self.day_field)
        self.day_set_button = QtWidgets.QPushButton(self.day_frame)
        self.day_set_button.setEnabled(False)
        self.day_set_button.setMaximumSize(QtCore.QSize(55, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        self.day_set_button.setFont(font)
        self.day_set_button.setObjectName("day_set_button")
        self.horizontalLayout_4.addWidget(self.day_set_button)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_meta = QtWidgets.QLabel(self.day_frame)
        self.label_meta.setEnabled(False)
        self.label_meta.setMinimumSize(QtCore.QSize(50, 0))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.label_meta.setFont(font)
        self.label_meta.setObjectName("label_meta")
        self.horizontalLayout_3.addWidget(self.label_meta)
        self.meta_field = QtWidgets.QPlainTextEdit(self.day_frame)
        self.meta_field.setEnabled(False)
        self.meta_field.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.meta_field.setFont(font)
        self.meta_field.setObjectName("meta_field")
        self.horizontalLayout_3.addWidget(self.meta_field)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_blocks = QtWidgets.QLabel(self.day_frame)
        self.label_blocks.setEnabled(False)
        self.label_blocks.setMinimumSize(QtCore.QSize(50, 0))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.label_blocks.setFont(font)
        self.label_blocks.setObjectName("label_blocks")
        self.horizontalLayout_6.addWidget(self.label_blocks)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.block_list = QtWidgets.QListWidget(self.day_frame)
        self.block_list.setEnabled(False)
        self.block_list.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.block_list.setFont(font)
        self.block_list.setObjectName("block_list")
        self.verticalLayout_2.addWidget(self.block_list)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.new_block_button = QtWidgets.QPushButton(self.day_frame)
        self.new_block_button.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.new_block_button.setFont(font)
        self.new_block_button.setObjectName("new_block_button")
        self.horizontalLayout_5.addWidget(self.new_block_button)
        self.edit_block_button = QtWidgets.QPushButton(self.day_frame)
        self.edit_block_button.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.edit_block_button.setFont(font)
        self.edit_block_button.setObjectName("edit_block_button")
        self.horizontalLayout_5.addWidget(self.edit_block_button)
        self.delete_block_button = QtWidgets.QPushButton(self.day_frame)
        self.delete_block_button.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.delete_block_button.setFont(font)
        self.delete_block_button.setObjectName("delete_block_button")
        self.horizontalLayout_5.addWidget(self.delete_block_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 3, 0, 1, 1)
        self.gridLayout_5.addWidget(self.day_frame, 1, 2, 1, 1)

        self.retranslateUi(Day)
        QtCore.QMetaObject.connectSlotsByName(Day)

    def retranslateUi(self, Day):
        _translate = QtCore.QCoreApplication.translate
        Day.setWindowTitle(_translate("Day", "Form"))
        self.label_2.setText(_translate("Day", "diary-survey-bot | survey-editor"))
        self.settings_button.setText(_translate("Day", "Settings"))
        self.recent_projects_headline.setText(_translate("Day", "Recent Projects"))
        self.headline_languages.setText(_translate("Day", "Languages"))
        self.iso_label.setText(_translate("Day", "ISO-639-1"))
        self.lang_field.setPlaceholderText(_translate("Day", "language"))
        self.lang_add_button.setText(_translate("Day", "add"))
        self.lang_delete_button.setText(_translate("Day", "delete"))
        self.templates_button.setText(_translate("Day", "Templates"))
        self.healdline_project.setText(_translate("Day", "Project"))
        self.load_project_button.setText(_translate("Day", "load"))
        self.delete_project_button.setText(_translate("Day", "delete"))
        self.directory_display.setPlaceholderText(_translate("Day", "Choose project directory."))
        self.directory_tool.setText(_translate("Day", "..."))
        self.headline_days.setText(_translate("Day", "Days"))
        self.new_day_button.setText(_translate("Day", "new"))
        self.delete_day_button.setText(_translate("Day", "delete"))
        self.headline_day.setText(_translate("Day", "Day"))
        self.label_day.setText(_translate("Day", "Day"))
        self.day_set_button.setText(_translate("Day", "set"))
        self.label_meta.setText(_translate("Day", "Meta"))
        self.meta_field.setPlaceholderText(_translate("Day", "Fill in some meta information."))
        self.label_blocks.setText(_translate("Day", "Blocks"))
        self.new_block_button.setText(_translate("Day", "new"))
        self.edit_block_button.setText(_translate("Day", "edit"))
        self.delete_block_button.setText(_translate("Day", "delete"))


