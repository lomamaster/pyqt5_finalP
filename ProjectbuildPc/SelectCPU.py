# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SelectCPU.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import connectdb
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(811, 591)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(100, 50, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(670, 530, 91, 31))
        self.pushButton.setObjectName("pushButton")

        listCPU = connectdb.onlyCPUname()
        self.cmbCPUname = QtWidgets.QComboBox(Form)
        self.cmbCPUname.setGeometry(QtCore.QRect(360, 70, 331, 22))
        self.cmbCPUname.setObjectName("cmbCPUname")
        for i in listCPU:
            self.cmbCPUname.addItem(i)

        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(40, 100, 731, 411))
        self.tableWidget.setObjectName("tableWidget")
        data = connectdb.getCPUdata()
        row = len(data)
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setRowCount(row)
        temp = QtWidgets.QTableWidgetItem
        self.tableWidget.setHorizontalHeaderItem(0, temp("Name"))
        self.tableWidget.setHorizontalHeaderItem(1, temp("Manufacturer"))
        self.tableWidget.setHorizontalHeaderItem(2, temp("Core Count"))
        self.tableWidget.setHorizontalHeaderItem(3, temp("Threads Count"))
        self.tableWidget.setHorizontalHeaderItem(4, temp("Core Clock"))
        self.tableWidget.setHorizontalHeaderItem(5, temp("Socket"))
        self.tableWidget.setHorizontalHeaderItem(6, temp("BoostClock"))
        self.tableWidget.setHorizontalHeaderItem(7, temp("Micro Architecture"))
        self.tableWidget.setHorizontalHeaderItem(8, temp("Lithography"))
        self.tableWidget.setHorizontalHeaderItem(9, temp("Generation"))
        for i in range(0, row):
            for x in range(10):
                if x == 0:
                    self.tableWidget.setItem(i, x, temp(data[i-1]['Name']))
                elif x == 1:
                    self.tableWidget.setItem(i, x, temp(data[i-1]['Manufacturer']))
                elif x == 2:
                    self.tableWidget.setItem(i, x, temp(data[i-1]['Core Count']))
                elif x == 3:
                    self.tableWidget.setItem(i, x, temp(data[i-1]['Threads Count']))
                elif x == 4:
                    self.tableWidget.setItem(i, x, temp(data[i-1]['Core Clock']))
                elif x == 5:
                    self.tableWidget.setItem(i, x, temp(data[i-1]['Socket']))
                elif x == 6:
                    self.tableWidget.setItem(i, x, temp(data[i-1]['BoostClock']))
                elif x == 7:
                    self.tableWidget.setItem(i, x, temp(data[i-1]['Micro Architecture']))
                elif x == 8:
                    self.tableWidget.setItem(i, x, temp(data[i-1]['Lithography']))
                elif x == 9:
                    self.tableWidget.setItem(i, x, temp(data[i-1]['Generation']))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Select CPU"))
        self.label.setText(_translate("Form", "Select CPU"))
        self.pushButton.setText(_translate("Form", "Add"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
