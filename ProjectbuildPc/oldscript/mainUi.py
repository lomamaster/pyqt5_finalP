# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUi.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets

data = "Glodal"


class Ui_MainWindow(object):

    def openCPU(self):
        from oldscript.SelectCPU import Ui_Form
        self.windowcpu = QtWidgets.QDialog()
        self.uicpu = Ui_Form()
        self.uicpu.setupUi(self.windowcpu)
        self.windowcpu.show()
        if self.uicpu.pushButton.clicked:
            self.uicpu.senddata()
            self.getdata()


    def openMB(self):
        from oldscript.SelectMB import Ui_Form
        self.windowmb = QtWidgets.QWidget()
        self.uimb = Ui_Form()
        self.uimb.setupUi(self.windowmb)
        self.windowmb.show()

    def openGPU(self):
        from oldscript.SelectGPU import Ui_Form
        self.windowgpu = QtWidgets.QWidget()
        self.uigpu = Ui_Form()
        self.uigpu.setupUi(self.windowgpu)
        self.windowgpu.show()

    def openHDD(self):
        from oldscript.SelectHDD import Ui_Form
        self.windowhdd = QtWidgets.QWidget()
        self.uihdd = Ui_Form()
        self.uihdd.setupUi(self.windowhdd)
        self.windowhdd.show()

    def openPSU(self):
        from oldscript.SelectPSU import Ui_Form
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()

    def openRAM(self):
        from oldscript.SelectRAM import Ui_Form
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(965, 722)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.selectCPU = QtWidgets.QPushButton(self.centralwidget)
        self.selectCPU.setGeometry(QtCore.QRect(50, 50, 111, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectCPU.sizePolicy().hasHeightForWidth())
        self.selectCPU.setSizePolicy(sizePolicy)
        self.selectCPU.setObjectName("selectCPU")
        self.selectMainboard = QtWidgets.QPushButton(self.centralwidget)
        self.selectMainboard.setGeometry(QtCore.QRect(50, 120, 111, 71))
        self.selectMainboard.setObjectName("selectMainboard")
        self.selectRam = QtWidgets.QPushButton(self.centralwidget)
        self.selectRam.setGeometry(QtCore.QRect(50, 340, 111, 61))
        self.selectRam.setObjectName("selectRam")
        self.selectVGA = QtWidgets.QPushButton(self.centralwidget)
        self.selectVGA.setGeometry(QtCore.QRect(50, 410, 111, 61))
        self.selectVGA.setObjectName("selectVGA")
        self.selectPSU = QtWidgets.QPushButton(self.centralwidget)
        self.selectPSU.setGeometry(QtCore.QRect(50, 480, 111, 61))
        self.selectPSU.setObjectName("selectPSU")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(50, 550, 111, 51))
        self.pushButton_6.setObjectName("pushButton_6")
        self.selectHDD1 = QtWidgets.QPushButton(self.centralwidget)
        self.selectHDD1.setGeometry(QtCore.QRect(50, 200, 111, 61))
        self.selectHDD1.setObjectName("selectHDD1")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 70, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 140, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(190, 220, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(190, 360, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(190, 430, 47, 13))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(190, 500, 47, 13))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(190, 570, 47, 13))
        self.label_7.setObjectName("label_7")
        self.selectHDD1_2 = QtWidgets.QPushButton(self.centralwidget)
        self.selectHDD1_2.setGeometry(QtCore.QRect(50, 270, 111, 61))
        self.selectHDD1_2.setObjectName("selectHDD1_2")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(190, 290, 47, 13))
        self.label_8.setObjectName("label_8")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(700, 650, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(590, 650, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 965, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        self.selectCPU.clicked.connect(self.openCPU)
        self.selectMainboard.clicked.connect(self.openMB)
        self.selectRam.clicked.connect(self.openRAM)
        self.selectVGA.clicked.connect(self.openGPU)
        self.selectPSU.clicked.connect(self.openPSU)
        self.selectHDD1.clicked.connect(self.openHDD)
        self.pushButton_2.clicked.connect(self.getdata)

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
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
        self.label_5.setText(_translate("MainWindow", "TextLabel"))
        self.label_6.setText(_translate("MainWindow", "TextLabel"))
        self.label_7.setText(_translate("MainWindow", "TextLabel"))
        self.selectHDD1_2.setText(_translate("MainWindow", "HDD"))
        self.label_8.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton.setText(_translate("MainWindow", "Calculate"))
        self.pushButton_2.setText(_translate("MainWindow", "History"))

    def getdata(self):
        print(data)
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", data))
        print("displayed in label")

    # def getdata(self):
    #    from SelectCPU import sendcpudata
    #    _translate = QtCore.QCoreApplication.translate
    #    self.label.setText(_translate("MainWindow", sendcpudata))

    # def test(self):
    #    _translate = QtCore.QCoreApplication.translate
    #    self.label.setText(_translate("MainWindow", "tryed"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
