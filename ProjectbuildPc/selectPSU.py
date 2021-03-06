from PyQt5 import QtCore,QtWidgets,QtGui,uic,QtWidgets

import connectdb
import mainUi

class psuwindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi(r'Ui\SelectPSU.ui', self)
        self.setWindowTitle("PCbuildProject")
        self.setFixedSize(self.size())
        self.addSelected.clicked.connect(self.senddata)
        self.pushreset.clicked.connect(self.reset_pressed)
        self.tableWidget.setColumnCount(6)
        temp = QtWidgets.QTableWidgetItem

        power = connectdb.onlyPower()
        for i in power:
            self.comboBox.addItem(i)
        self.showData()
        self.comboBox.currentIndexChanged.connect(self.selectedData)
        self.pushBack.clicked.connect(self.getBack)

    def getBack(self):
        self.hide()
        self.ui = mainUi.mainwindow()
        self.ui.show()

    def showData(self):
        # self.currentTextChanged.connect(self.selectedtype)
        data = connectdb.getPSUdata()
        print("pulled data psu")
        row = len(data)
        print("set data")
        # self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(row)
        print("set row")
        temp = QtWidgets.QTableWidgetItem
        print("set temp")
        self.tableWidget.setHorizontalHeaderItem(0, temp("Name"))
        self.tableWidget.setHorizontalHeaderItem(1, temp("Power"))
        self.tableWidget.setHorizontalHeaderItem(2, temp("Certification"))
        self.tableWidget.setHorizontalHeaderItem(3, temp("Modular"))
        self.tableWidget.setHorizontalHeaderItem(4, temp("Form Factor"))
        self.tableWidget.setHorizontalHeaderItem(5, temp("  "))
        print("set header")
        for i in range(0, row):
            for x in range(6):
                if x == 0:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['Name']))
                elif x == 1:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['Power']))
                elif x == 2:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['Certification']))
                elif x == 3:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['Modular']))
                elif x == 4:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['Form Factor']))
                elif x == 5:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['Score']))
                    self.tableWidget.item(i, x).setForeground(QtGui.QColor(255, 255, 255))


    def reset_pressed(self):
        self.showData()

    def selectedData(self):
        selected = str(self.comboBox.currentText())
        print(selected)
        print(type(selected))
        # self.currentTextChanged.connect(self.selectedtype)
        data = connectdb.getPSUdata(selected)
        print("pulled data psu")
        row = len(data)
        print("set data")
        # self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(row)
        print("set row")
        temp = QtWidgets.QTableWidgetItem
        print("set temp")
        self.tableWidget.setHorizontalHeaderItem(0, temp("Name"))
        self.tableWidget.setHorizontalHeaderItem(1, temp("Power"))
        self.tableWidget.setHorizontalHeaderItem(2, temp("Certification"))
        self.tableWidget.setHorizontalHeaderItem(3, temp("Modular"))
        self.tableWidget.setHorizontalHeaderItem(4, temp("Form Factor"))
        self.tableWidget.setHorizontalHeaderItem(5, temp("  "))
        print("set header")
        for i in range(0, row):
            for x in range(6):
                if x == 0:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['Name']))
                elif x == 1:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['Power']))
                elif x == 2:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['Certification']))
                elif x == 3:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['Modular']))
                elif x == 4:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['Form Factor']))
                elif x == 5:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['Score']))
                    self.tableWidget.item(i, x).setForeground(QtGui.QColor(255, 255, 255))



    def senddata(self):
        data = self.tableWidget.selectedItems()
        for item in data:
            print(item.text())
        setdata = "{} {}".format(data[1].text(),data[0].text())
        print(setdata)
        self.hide()
        self.ui = mainUi.mainwindow()
        mainUi.psuname = str(setdata)
        self.ui.show()
        self.ui.lblpsu.setText("{}".format(setdata))
        mainUi.psuscore = data[5].text()
        print(mainUi.psuscore)
