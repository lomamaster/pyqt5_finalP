from PyQt5 import QtCore,QtWidgets,QtGui,uic,QtWidgets

import connectdb
import mainUi

class ramwindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi(r'Ui\SelectRAM.ui', self)
        self.setWindowTitle("PCbuildProject")
        self.setFixedSize(self.size())
        self.addSelected.clicked.connect(self.senddata)
        self.pushreset.clicked.connect(self.reset_pressed)
        self.tableWidget.setColumnCount(7)
        temp = QtWidgets.QTableWidgetItem

        ddr = connectdb.onlyDDR()
        for i in ddr:
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
        data = connectdb.getRAMdata()
        print("pulled data ram")
        row = len(data)
        print("set data")
        # self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(row)
        print("set row")
        temp = QtWidgets.QTableWidgetItem
        print("set temp")
        self.tableWidget.setHorizontalHeaderItem(0, temp("Name"))
        self.tableWidget.setHorizontalHeaderItem(1, temp("Manufacturer"))
        self.tableWidget.setHorizontalHeaderItem(2, temp("DDR"))
        self.tableWidget.setHorizontalHeaderItem(3, temp("BUS"))
        self.tableWidget.setHorizontalHeaderItem(4, temp("CL"))
        self.tableWidget.setHorizontalHeaderItem(5, temp("capacity"))
        self.tableWidget.setHorizontalHeaderItem(6, temp("  "))
        print("set header")
        for i in range(0, row):
            for x in range(7):
                if x == 0:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['Name']))
                elif x == 1:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['Manufacturer']))
                elif x == 2:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['DDR']))
                elif x == 3:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['BUS']))
                elif x == 4:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['CL']))
                elif x == 5:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['capacity']))
                elif x == 6:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['Score']))
                    self.tableWidget.item(i, x).setForeground(QtGui.QColor(255, 255, 255))


    def reset_pressed(self):
        self.showData()

    def selectedData(self):
        selectedddr = str(self.comboBox.currentText())
        print(selectedddr)
        print(type(selectedddr))
        # self.currentTextChanged.connect(self.selectedtype)
        data = connectdb.getRAMddrdata(selectedddr)
        print("pulled data ram")
        row = len(data)
        print("set data")
        # self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(row)
        print("set row")
        temp = QtWidgets.QTableWidgetItem
        print("set temp")
        self.tableWidget.setHorizontalHeaderItem(0, temp("Name"))
        self.tableWidget.setHorizontalHeaderItem(1, temp("Manufacturer"))
        self.tableWidget.setHorizontalHeaderItem(2, temp("DDR"))
        self.tableWidget.setHorizontalHeaderItem(3, temp("BUS"))
        self.tableWidget.setHorizontalHeaderItem(4, temp("CL"))
        self.tableWidget.setHorizontalHeaderItem(5, temp("capacity"))
        self.tableWidget.setHorizontalHeaderItem(6, temp("  "))
        print("set header")
        for i in range(0, row):
            for x in range(7):
                if x == 0:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['Name']))
                elif x == 1:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['Manufacturer']))
                elif x == 2:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['DDR']))
                elif x == 3:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['BUS']))
                elif x == 4:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['CL']))
                elif x == 5:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['capacity']))
                elif x == 6:
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
        mainUi.ramname = str(setdata)
        self.ui.show()
        self.ui.lblram.setText("{}".format(setdata))
        mainUi.ramscore = data[6].text()
        print(mainUi.ramscore)