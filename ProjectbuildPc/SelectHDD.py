# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SelectRAM.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import connectdb
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(860, 649)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(170, 40, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(670, 590, 75, 23))
        self.pushButton.setObjectName("pushButton")

        typeHdd = connectdb.onlyHDDtype()
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(540, 60, 121, 22))
        self.comboBox.setObjectName("comboBox")
        for i in typeHdd:
            self.comboBox.addItem(i)

        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(20, 140, 821, 401))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)

        self.comboBox.currentIndexChanged.connect(self.showData)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def showData(self, selectedtype):
        print(selectedtype)
        #self.currentTextChanged.connect(self.selectedtype)
        if selectedtype == 0:
                data = connectdb.getSSDdata()
                row = len(data)
                #self.tableWidget.setColumnCount(7)
                self.tableWidget.setRowCount(row)
                temp = QtWidgets.QTableWidgetItem
                self.tableWidget.setHorizontalHeaderItem(0, temp("Name"))
                self.tableWidget.setHorizontalHeaderItem(1, temp("Manufacturer"))
                self.tableWidget.setHorizontalHeaderItem(2, temp("format"))
                self.tableWidget.setHorizontalHeaderItem(3, temp("Interface"))
                self.tableWidget.setHorizontalHeaderItem(4, temp("Capacity"))
                self.tableWidget.setHorizontalHeaderItem(5, temp("Read"))
                self.tableWidget.setHorizontalHeaderItem(6, temp("Write"))
                for i in range(0, row):
                    for x in range(7):
                        if x == 0:
                            self.tableWidget.setItem(i, x, temp(data[i - 1]['Name']))
                        elif x == 1:
                            self.tableWidget.setItem(i, x, temp(data[i - 1]['Manufacturer']))
                        elif x == 2:
                            self.tableWidget.setItem(i, x, temp(data[i - 1]['format']))
                        elif x == 3:
                            self.tableWidget.setItem(i, x, temp(data[i - 1]['Interface']))
                        elif x == 4:
                            self.tableWidget.setItem(i, x, temp(data[i - 1]['Capacity']))
                        elif x == 5:
                            self.tableWidget.setItem(i, x, temp(data[i - 1]['Read']))
                        elif x == 6:
                            self.tableWidget.setItem(i, x, temp(data[i - 1]['Write']))
        elif selectedtype == 1:
                data = connectdb.getHDDdata()
                row = len(data)
                #self.tableWidget.setColumnCount(8)
                self.tableWidget.setRowCount(row)
                temp = QtWidgets.QTableWidgetItem
                self.tableWidget.setHorizontalHeaderItem(0, temp("Name"))
                self.tableWidget.setHorizontalHeaderItem(1, temp("Manufacturer"))
                self.tableWidget.setHorizontalHeaderItem(2, temp("format"))
                self.tableWidget.setHorizontalHeaderItem(3, temp("Interface"))
                self.tableWidget.setHorizontalHeaderItem(4, temp("Capacity"))
                self.tableWidget.setHorizontalHeaderItem(5, temp("Read"))
                self.tableWidget.setHorizontalHeaderItem(6, temp("Write"))
                self.tableWidget.setHorizontalHeaderItem(7, temp("RPM"))
                for i in range(0, row):
                    for x in range(8):
                        if x == 0:
                            self.tableWidget.setItem(i, x, temp(data[i - 1]['Name']))
                        elif x == 1:
                            self.tableWidget.setItem(i, x, temp(data[i - 1]['Manufacturer']))
                        elif x == 2:
                            self.tableWidget.setItem(i, x, temp(data[i - 1]['format']))
                        elif x == 3:
                            self.tableWidget.setItem(i, x, temp(data[i - 1]['Interface']))
                        elif x == 4:
                            self.tableWidget.setItem(i, x, temp(data[i - 1]['Capacity']))
                        elif x == 5:
                            self.tableWidget.setItem(i, x, temp(data[i - 1]['Read']))
                        elif x == 6:
                            self.tableWidget.setItem(i, x, temp(data[i - 1]['Write']))
                        elif x == 7:
                            self.tableWidget.setItem(i, x, temp(data[i - 1]['RPM']))
        elif selectedtype == 2:
                data = connectdb.getHDDdata()
                row = len(data)
                #self.tableWidget.setColumnCount(8)
                self.tableWidget.setRowCount(row)
                temp = QtWidgets.QTableWidgetItem
                self.tableWidget.setHorizontalHeaderItem(0, temp("Name"))
                self.tableWidget.setHorizontalHeaderItem(1, temp("Manufacturer"))
                self.tableWidget.setHorizontalHeaderItem(2, temp("format"))
                self.tableWidget.setHorizontalHeaderItem(3, temp("Interface"))
                self.tableWidget.setHorizontalHeaderItem(4, temp("Capacity"))
                self.tableWidget.setHorizontalHeaderItem(5, temp("Read"))
                self.tableWidget.setHorizontalHeaderItem(6, temp("Write"))
                self.tableWidget.setHorizontalHeaderItem(7, temp("RPM"))
                for i in range(0, row):
                    for x in range(8):
                        if x == 0:
                            self.tableWidget.setItem(i, x, temp(data[i - 1]['Name']))
                        elif x == 1:
                            self.tableWidget.setItem(i, x, temp(data[i - 1]['Manufacturer']))
                        elif x == 2:
                            self.tableWidget.setItem(i, x, temp(data[i - 1]['format']))
                        elif x == 3:
                            self.tableWidget.setItem(i, x, temp(data[i - 1]['interface']))
                        elif x == 4:
                            self.tableWidget.setItem(i, x, temp(data[i - 1]['capacity']))
                        elif x == 5:
                            self.tableWidget.setItem(i, x, temp(data[i - 1]['Read']))
                        elif x == 6:
                            self.tableWidget.setItem(i, x, temp(data[i - 1]['Write']))
                        elif x == 7:
                            self.tableWidget.setItem(i, x, temp(data[i - 1]['RPM']))



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Select HDD"))
        self.pushButton.setText(_translate("Form", "Select"))



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
