# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(556, 578)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textField = QtWidgets.QListWidget(self.centralwidget)
        self.textField.setObjectName("textField")
        self.verticalLayout.addWidget(self.textField)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonLeft = QtWidgets.QPushButton(self.centralwidget)
        self.buttonLeft.setMouseTracking(True)
        self.buttonLeft.setObjectName("buttonLeft")
        self.horizontalLayout.addWidget(self.buttonLeft)
        self.buttonRight = QtWidgets.QPushButton(self.centralwidget)
        self.buttonRight.setObjectName("buttonRight")
        self.horizontalLayout.addWidget(self.buttonRight)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.buttonLeft.setText(_translate("MainWindow", "left"))
        self.buttonRight.setText(_translate("MainWindow", "right"))

