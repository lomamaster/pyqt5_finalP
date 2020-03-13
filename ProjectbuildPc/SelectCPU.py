from PyQt5 import QtCore,QtWidgets,QtGui,uic,QtWidgets
from PyQt5.QtGui import QBrush, QColor

import connectdb
import mainUi


class cpuwindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi(r'Ui\SelectCPU.ui', self)
        self.setWindowTitle("PCbuildProject")
        self.setFixedSize(self.size())
        self.addSelected.clicked.connect(self.senddata)
        data = connectdb.getCPUdata()
        row = len(data)
        self.tableWidget.setColumnCount(11)
        self.tableWidget.setRowCount(row)
        CPUmanu = connectdb.onlyCPUmanu()
        for i in CPUmanu:
            self.cmbbrand.addItem(i)
        self.showData()
        self.cmbbrand.currentIndexChanged.connect(self.selectedData)
        self.pushBack.clicked.connect(self.getBack)

    def showData(self):
        data = connectdb.getCPUdata()
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
        self.tableWidget.setHorizontalHeaderItem(2, temp("Core Count"))
        self.tableWidget.setHorizontalHeaderItem(3, temp("Threads Count"))
        self.tableWidget.setHorizontalHeaderItem(4, temp("Core Clock"))
        self.tableWidget.setHorizontalHeaderItem(5, temp("Socket"))
        self.tableWidget.setHorizontalHeaderItem(6, temp("BoostClock"))
        self.tableWidget.setHorizontalHeaderItem(7, temp("Micro Architecture"))
        self.tableWidget.setHorizontalHeaderItem(8, temp("Lithography"))
        self.tableWidget.setHorizontalHeaderItem(9, temp("Generation"))
        self.tableWidget.setHorizontalHeaderItem(10, temp("     "))
        for i in range(0, row):
            for x in range(11):
                if x == 0:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['Name']))
                elif x == 1:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['Manufacturer']))
                elif x == 2:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['Core Count']))
                elif x == 3:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['Threads Count']))
                elif x == 4:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['Core Clock']))
                elif x == 5:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['Socket']))
                elif x == 6:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['BoostClock']))
                elif x == 7:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['Micro Architecture']))
                elif x == 8:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['Lithography']))
                elif x == 9:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['Generation']))
                elif x == 10:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['Score']))
                    self.tableWidget.item(i, x).setForeground(QtGui.QColor(255, 255, 255))

    def selectedData(self):
        selectedmanu = str(self.cmbbrand.currentText())
        print(selectedmanu)
        print(type(selectedmanu))
        # self.currentTextChanged.connect(self.selectedtype)
        data = connectdb.getSelectCPUdata(selectedmanu)
        print("pulled data cpu")
        row = len(data)
        print("set data")
        # self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(row)
        print("set row")
        temp = QtWidgets.QTableWidgetItem
        print("set temp")
        for i in range(0, row):
            for x in range(11):
                if x == 0:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['Name']))
                elif x == 1:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['Manufacturer']))
                elif x == 2:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['Core Count']))
                elif x == 3:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['Threads Count']))
                elif x == 4:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['Core Clock']))
                elif x == 5:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['Socket']))
                elif x == 6:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['BoostClock']))
                elif x == 7:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['Micro Architecture']))
                elif x == 8:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['Lithography']))
                elif x == 9:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['Generation']))
                elif x == 10:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['Score']))
                    self.tableWidget.item(i, x).setForeground(QtGui.QColor(255, 255, 255))

    def senddata(self):
        data = self.tableWidget.selectedItems()
        setdata = "{} {} {}".format(data[9].text(),data[1].text(),data[0].text())
        print(setdata)
        self.hide()
        self.ui = mainUi.mainwindow()
        mainUi.cpuname = str(setdata)
        self.ui.show()
        self.ui.lblcpu.setText("{}".format(setdata))
        mainUi.cpuscore = data[10].text()
        print(mainUi.cpuscore)

    def getBack(self):
        self.hide()
        self.ui = mainUi.mainwindow()
        self.ui.show()
