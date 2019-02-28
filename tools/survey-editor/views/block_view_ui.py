# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'block.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Block(object):
    def setupUi(self, Block):
        Block.setObjectName("Block")
        Block.resize(1366, 768)
        self.frame = QtWidgets.QFrame(Block)
        self.frame.setGeometry(QtCore.QRect(10, 10, 241, 101))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.headline = QtWidgets.QLabel(self.frame)
        self.headline.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.headline.setFont(font)
        self.headline.setAlignment(QtCore.Qt.AlignCenter)
        self.headline.setObjectName("headline")
        self.gridLayout.addWidget(self.headline, 0, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(Block)
        self.frame_2.setGeometry(QtCore.QRect(10, 120, 241, 641))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.tabWidget = QtWidgets.QTabWidget(Block)
        self.tabWidget.setGeometry(QtCore.QRect(260, 10, 1100, 600))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.frame_3 = QtWidgets.QFrame(Block)
        self.frame_3.setGeometry(QtCore.QRect(260, 620, 1101, 141))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")

        self.retranslateUi(Block)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Block)

    def retranslateUi(self, Block):
        _translate = QtCore.QCoreApplication.translate
        Block.setWindowTitle(_translate("Block", "Form"))
        self.headline.setText(_translate("Block", "Block X"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Block", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Block", "Tab 2"))


