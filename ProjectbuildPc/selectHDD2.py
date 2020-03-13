from PyQt5 import QtCore,QtWidgets,QtGui,uic,QtWidgets

import connectdb
import mainUi


class hdd2window(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi(r'Ui\SelectHDD.ui', self)
        self.setWindowTitle("PCbuildProject")
        self.setFixedSize(self.size())
        self.addSelected.clicked.connect(self.senddata)
        typeHdd = connectdb.onlyHDDtype()
        for i in typeHdd:
            self.cmbHDD.addItem(i)
        self.tableWidget.setColumnCount(9)
        temp = QtWidgets.QTableWidgetItem
        self.showData(str(self.cmbHDD.currentText()))
        self.cmbHDD.currentTextChanged.connect(self.showData)
        self.pushBack.clicked.connect(self.getBack)

    def showData(self, selectedtype):
        print(selectedtype)
        print(type(selectedtype))
        #self.currentTextChanged.connect(self.selectedtype)
        if selectedtype == "SSD":
                data = connectdb.getSSDdata()
                print("pulled data ssd")
                row = len(data)
                print("set data")
                #self.tableWidget.setColumnCount(7)
                self.tableWidget.setRowCount(row)
                print("set row")
                temp = QtWidgets.QTableWidgetItem
                print("set temp")
                self.tableWidget.setHorizontalHeaderItem(0, temp("Name"))
                self.tableWidget.setHorizontalHeaderItem(1, temp("Manufacturer"))
                self.tableWidget.setHorizontalHeaderItem(2, temp("format"))
                self.tableWidget.setHorizontalHeaderItem(3, temp("Interface"))
                self.tableWidget.setHorizontalHeaderItem(4, temp("Capacity"))
                self.tableWidget.setHorizontalHeaderItem(5, temp("Read"))
                self.tableWidget.setHorizontalHeaderItem(6, temp("Write"))
                self.tableWidget.setHorizontalHeaderItem(7, temp("      "))
                self.tableWidget.setHorizontalHeaderItem(8, temp("      "))
                print("set header")
                for i in range(0, row):
                    for x in range(9):
                        if x == 0:
                            self.tableWidget.setItem(i, x, temp(data[i - 1]['Name']))
                        elif x == 1:
                            self.tableWidget.setItem(i, x, temp(data[i - 1]['Manufacturer']))
                        elif x == 2:
                            self.tableWidget.setItem(i, x, temp(data[i - 1]['Format']))
                        elif x == 3:
                            self.tableWidget.setItem(i, x, temp(data[i - 1]['Interface']))
                        elif x == 4:
                            self.tableWidget.setItem(i, x, temp(data[i - 1]['Capacity']))
                        elif x == 5:
                            self.tableWidget.setItem(i, x, temp(data[i - 1]['Read']))
                        elif x == 6:
                            self.tableWidget.setItem(i, x, temp(data[i - 1]['Write']))
                        elif x == 7:
                            self.tableWidget.setItem(i, x, temp(" "))
                        elif x == 8:
                            self.tableWidget.setItem(i, x, temp(data[i - 1]['Score']))
                            self.tableWidget.item(i, x).setForeground(QtGui.QColor(255, 255, 255))
        elif selectedtype == "HDD":
                data = connectdb.getHDDdata()
                print("pulled data hdd")
                row = len(data)
                #self.tableWidget.setColumnCount(8)
                self.tableWidget.setRowCount(row)
                temp = QtWidgets.QTableWidgetItem
                self.tableWidget.setHorizontalHeaderItem(0, temp("Name"))
                self.tableWidget.setHorizontalHeaderItem(1, temp("Manufacturer"))
                self.tableWidget.setHorizontalHeaderItem(2, temp("Format"))
                self.tableWidget.setHorizontalHeaderItem(3, temp("Interface"))
                self.tableWidget.setHorizontalHeaderItem(4, temp("Capacity"))
                self.tableWidget.setHorizontalHeaderItem(5, temp("Read"))
                self.tableWidget.setHorizontalHeaderItem(6, temp("Write"))
                self.tableWidget.setHorizontalHeaderItem(7, temp("RPM"))
                self.tableWidget.setHorizontalHeaderItem(8, temp("      "))
                for i in range(0, row):
                    for x in range(9):
                        if x == 0:
                            self.tableWidget.setItem(i, x, temp(data[i - 1]['Name']))
                        elif x == 1:
                            self.tableWidget.setItem(i, x, temp(data[i - 1]['Manufacturer']))
                        elif x == 2:
                            self.tableWidget.setItem(i, x, temp(data[i - 1]['Format']))
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
                        elif x == 8:
                            self.tableWidget.setItem(i, x, temp(data[i - 1]['Score']))
                            self.tableWidget.item(i, x).setForeground(QtGui.QColor(255, 255, 255))
        elif selectedtype == "SSHD":
                data = connectdb.getSSHDdata()
                print("pulled data ssdh")
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
                self.tableWidget.setHorizontalHeaderItem(8, temp("      "))
                for i in range(0, row):
                    for x in range(9):
                        if x == 0:
                            self.tableWidget.setItem(i, x, temp(data[i - 1]['Name']))
                        elif x == 1:
                            self.tableWidget.setItem(i, x, temp(data[i - 1]['Manufacturer']))
                        elif x == 2:
                            self.tableWidget.setItem(i, x, temp(data[i - 1]['Format']))
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
                        elif x == 8:
                            self.tableWidget.setItem(i, x, temp(data[i - 1]['Score']))
                            self.tableWidget.item(i, x).setForeground(QtGui.QColor(255, 255, 255))

    def senddata(self):
        data = self.tableWidget.selectedItems()
        for item in data:
            print(item.text())
        setdata = "{} {} {}".format(data[1].text(), data[0].text(), data[3].text())
        scoredata = float(data[8].text())
        print(setdata)
        self.hide()
        self.ui = mainUi.mainwindow()
        mainUi.hdd2name = str(setdata)
        self.ui.show()
        self.ui.lblhdd_2.setText("{}".format(setdata))
        if mainUi.hddscore < scoredata:
            mainUi.hddscore = scoredata
        print(mainUi.hddscore)

    def getBack(self):
        self.hide()
        self.ui = mainUi.mainwindow()
        self.ui.show()