from PyQt5 import QtCore,QtWidgets,QtGui,uic,QtWidgets

import connectdb
import mainUi


class mbwindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi(r'Ui\SelectMB.ui', self)
        self.setWindowTitle("PCbuildProject")
        self.setFixedSize(self.size())
        self.addSelected.clicked.connect(self.senddata)
        self.pushreset.clicked.connect(self.reset_pressed)
        self.pushBack.clicked.connect(self.getBack)
        self.tableWidget.setColumnCount(10)
        temp = QtWidgets.QTableWidgetItem

        chipsetMB = connectdb.onlyMBchipset()
        for i in chipsetMB:
            self.comboBox.addItem(i)
        self.showData()
        self.comboBox.currentIndexChanged.connect(self.selectedData)

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
        self.tableWidget.setHorizontalHeaderItem(9, temp("  "))
        print("set header")
        for i in range(0, row):
            for x in range(10):
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
                elif x == 9:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['Score']))
                    self.tableWidget.item(i, x).setForeground(QtGui.QColor(255, 255, 255))

    def reset_pressed(self):
        self.showData()

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
        self.tableWidget.setHorizontalHeaderItem(9, temp("  "))
        print("set header")
        for i in range(0, row):
            for x in range(10):
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
                elif x == 9:
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
        mainUi.mbname = str(setdata)
        self.ui.show()
        self.ui.lblmb.setText("{}".format(setdata))
        mainUi.mbscore = data[9].text()
        print(mainUi.mbscore)

    def getBack(self):
        self.hide()
        self.ui = mainUi.mainwindow()
        self.ui.show()
