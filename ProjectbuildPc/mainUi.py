# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUi.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import pymongo
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):

    def openCPU(self):
        from SelectCPU import Ui_Form
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(965, 722)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #CPUbutton
        self.selectCPU = QtWidgets.QPushButton(self.centralwidget)
        self.selectCPU.setGeometry(QtCore.QRect(50, 50, 451, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectCPU.sizePolicy().hasHeightForWidth())
        self.selectCPU.setSizePolicy(sizePolicy)
        self.selectCPU.setObjectName("selectCPU")
        self.selectCPU.clicked.connect(self.openCPU)

        #MBbutton
        self.selectMainboard = QtWidgets.QPushButton(self.centralwidget)
        self.selectMainboard.setGeometry(QtCore.QRect(50, 120, 451, 71))
        self.selectMainboard.setObjectName("selectMainboard")

        #RAMbutton
        self.selectRam = QtWidgets.QPushButton(self.centralwidget)
        self.selectRam.setGeometry(QtCore.QRect(50, 270, 451, 61))
        self.selectRam.setObjectName("selectRam")

        #VGAbutton
        self.selectVGA = QtWidgets.QPushButton(self.centralwidget)
        self.selectVGA.setGeometry(QtCore.QRect(50, 340, 451, 61))
        self.selectVGA.setObjectName("selectVGA")

        #PSUbutton
        self.selectPSU = QtWidgets.QPushButton(self.centralwidget)
        self.selectPSU.setGeometry(QtCore.QRect(50, 410, 451, 61))
        self.selectPSU.setObjectName("selectPSU")

        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(50, 480, 451, 51))
        self.pushButton_6.setObjectName("pushButton_6")

        # HDDbutton
        self.selectHDD1 = QtWidgets.QPushButton(self.centralwidget)
        self.selectHDD1.setGeometry(QtCore.QRect(50, 200, 451, 61))
        self.selectHDD1.setObjectName("selectHDD1")
        MainWindow.setCentralWidget(self.centralwidget)


        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 965, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.selectCPU.setText(_translate("MainWindow", "CPU"))
        self.selectMainboard.setText(_translate("MainWindow", "Mainboard"))
        self.selectRam.setText(_translate("MainWindow", "RAM"))
        self.selectVGA.setText(_translate("MainWindow", "VGA"))
        self.selectPSU.setText(_translate("MainWindow", "PSU"))
        self.pushButton_6.setText(_translate("MainWindow", "SINK CPU"))
        self.selectHDD1.setText(_translate("MainWindow", "HDD"))

    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Hello world")
        msg.setText("Hello again")

        x = msg.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
