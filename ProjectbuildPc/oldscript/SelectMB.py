# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SelectMB.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

import connectdb


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(739, 617)

        self.pushreset = QtWidgets.QPushButton(Form)
        self.pushreset.setGeometry(QtCore.QRect(550, 40, 75, 23))
        self.pushreset.setObjectName("pushreset")
        self.pushreset.clicked.connect(self.reset_pressed)

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(600, 560, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 40, 91, 16))
        self.label.setObjectName("label")

        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(20, 110, 701, 431))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        chipsetMB = connectdb.onlyMBchipset()
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(280, 40, 181, 22))
        self.comboBox.setObjectName("comboBox")
        self.tableWidget.setColumnCount(9)
        for i in chipsetMB:
            self.comboBox.addItem(i)

        self.showData()
        self.comboBox.currentIndexChanged.connect(self.selectedData)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def reset_pressed(self):
        self.showData()

    def showData(self):
        # self.currentTextChanged.connect(self.selectedtype)
        data = connectdb.getMBdata()
        print("pulled data mb")
        row = len(data)
        print("set data")
        # self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(row)
        print("set row")
        temp = QtWidgets.QTableWidgetItem
        print("set temp")
        self.tableWidget.setHorizontalHeaderItem(0, temp("Name"))
        self.tableWidget.setHorizontalHeaderItem(1, temp("Manufacturer"))
        self.tableWidget.setHorizontalHeaderItem(2, temp("chipset"))
        self.tableWidget.setHorizontalHeaderItem(3, temp("Ram Slot"))
        self.tableWidget.setHorizontalHeaderItem(4, temp("Socket"))
        self.tableWidget.setHorizontalHeaderItem(5, temp("DDR"))
        self.tableWidget.setHorizontalHeaderItem(6, temp("Support Bus"))
        self.tableWidget.setHorizontalHeaderItem(7, temp("Audio"))
        self.tableWidget.setHorizontalHeaderItem(8, temp("Wireless Support"))
        print("set header")
        for i in range(0, row):
            for x in range(9):
                if x == 0:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['Name']))
                elif x == 1:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['Manufacturer']))
                elif x == 2:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['chipset']))
                elif x == 3:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['Ram Slot']))
                elif x == 4:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['Socket']))
                elif x == 5:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['DDR']))
                elif x == 6:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['Support Bus']))
                elif x == 7:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['Audio']))
                elif x == 8:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['Wireless Support']))

    def selectedData(self):
        selectedchipset = str(self.comboBox.currentText())
        print(selectedchipset)
        print(type(selectedchipset))
        # self.currentTextChanged.connect(self.selectedtype)
        data = connectdb.getSelectedMBdata(selectedchipset)
        print("pulled data ssd")
        row = len(data)
        print("set data")
        # self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(row)
        print("set row")
        temp = QtWidgets.QTableWidgetItem
        print("set temp")
        self.tableWidget.setHorizontalHeaderItem(0, temp("Name"))
        self.tableWidget.setHorizontalHeaderItem(1, temp("Manufacturer"))
        self.tableWidget.setHorizontalHeaderItem(2, temp("chipset"))
        self.tableWidget.setHorizontalHeaderItem(3, temp("Ram Slot"))
        self.tableWidget.setHorizontalHeaderItem(4, temp("Socket"))
        self.tableWidget.setHorizontalHeaderItem(5, temp("DDR"))
        self.tableWidget.setHorizontalHeaderItem(6, temp("Support Bus"))
        self.tableWidget.setHorizontalHeaderItem(7, temp("Audio"))
        self.tableWidget.setHorizontalHeaderItem(8, temp("Wireless Support"))
        print("set header")
        for i in range(0, row):
            for x in range(9):
                if x == 0:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['Name']))
                elif x == 1:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['Manufacturer']))
                elif x == 2:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['chipset']))
                elif x == 3:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['Ram Slot']))
                elif x == 4:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['Socket']))
                elif x == 5:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['DDR']))
                elif x == 6:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['Support Bus']))
                elif x == 7:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['Audio']))
                elif x == 8:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['Wireless Support']))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "select"))
        self.pushreset.setText(_translate("Form", "reset"))
        self.label.setText(_translate("Form", "Select Mainboard"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

