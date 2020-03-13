from PyQt5 import QtCore,QtWidgets,QtGui,uic,QtWidgets

import connectdb
import mainUi


class sinkwindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi(r'Ui\SelectSink.ui', self)
        self.setWindowTitle("PCbuildProject")
        self.setFixedSize(self.size())
        self.addSelected.clicked.connect(self.senddata)
        self.tableWidget.setColumnCount(7)
        temp = QtWidgets.QTableWidgetItem

        series = connectdb.onlySinktype()
        for i in series:
            self.comboBox.addItem(i)
        self.showData(str(self.comboBox.currentText()))
        self.comboBox.currentTextChanged.connect(self.showData)
        self.pushBack.clicked.connect(self.getBack)

    def getBack(self):
        self.hide()
        self.ui = mainUi.mainwindow()
        self.ui.show()

    def showData(self, selectedtype):
        print(selectedtype)
        print(type(selectedtype))
        #self.currentTextChanged.connect(self.selectedtype)
        if selectedtype == "Water cooling":
                data = connectdb.getLiqdata()
                print("pulled data liqu")
                row = len(data)
                print("set data")
                #self.tableWidget.setColumnCount(7)
                self.tableWidget.setRowCount(row)
                print("set row")
                temp = QtWidgets.QTableWidgetItem
                print("set temp")
                self.tableWidget.setHorizontalHeaderItem(0, temp("Name"))
                self.tableWidget.setHorizontalHeaderItem(1, temp("Sink Type"))
                self.tableWidget.setHorizontalHeaderItem(2, temp("FAN SPEED"))
                self.tableWidget.setHorizontalHeaderItem(3, temp("CONNECTOR"))
                self.tableWidget.setHorizontalHeaderItem(4, temp("Number of Fans"))
                self.tableWidget.setHorizontalHeaderItem(5, temp("pump speed"))
                self.tableWidget.setHorizontalHeaderItem(6, temp("  "))
                print("set header")
                for i in range(0, row):
                    for x in range(7):
                        if x == 0:
                            self.tableWidget.setItem(i, x, temp(data[i - 1]['Name']))
                        elif x == 1:
                            self.tableWidget.setItem(i, x, temp(data[i - 1]['Sink Type']))
                        elif x == 2:
                            self.tableWidget.setItem(i, x, temp(data[i - 1]['FAN SPEED']))
                        elif x == 3:
                            self.tableWidget.setItem(i, x, temp(data[i - 1]['CONNECTOR']))
                        elif x == 4:
                            self.tableWidget.setItem(i, x, temp(data[i - 1]['Number of Fans']))
                        elif x == 5:
                            self.tableWidget.setItem(i, x, temp(data[i - 1]['pump speed']))
                        elif x == 6:
                            self.tableWidget.setItem(i, x, temp(data[i - 1]['Score']))
                            self.tableWidget.item(i, x).setForeground(QtGui.QColor(255, 255, 255))

        elif selectedtype == "Air cooling":
                data = connectdb.getAirdata()
                print("pulled data Air")
                row = len(data)
                #self.tableWidget.setColumnCount(8)
                self.tableWidget.setRowCount(row)
                temp = QtWidgets.QTableWidgetItem
                self.tableWidget.setHorizontalHeaderItem(0, temp("Name"))
                self.tableWidget.setHorizontalHeaderItem(1, temp("Sink Type"))
                self.tableWidget.setHorizontalHeaderItem(2, temp("FAN SPEED"))
                self.tableWidget.setHorizontalHeaderItem(3, temp("CONNECTOR"))
                self.tableWidget.setHorizontalHeaderItem(4, temp("Number of Fans"))
                self.tableWidget.setHorizontalHeaderItem(5, temp("HEATPIPES"))
                self.tableWidget.setHorizontalHeaderItem(6, temp("  "))
                for i in range(0, row):
                    for x in range(7):
                        if x == 0:
                            self.tableWidget.setItem(i, x, temp(data[i - 1]['Name']))
                        elif x == 1:
                            self.tableWidget.setItem(i, x, temp(data[i - 1]['Sink Type']))
                        elif x == 2:
                            self.tableWidget.setItem(i, x, temp(data[i - 1]['FAN SPEED']))
                        elif x == 3:
                            self.tableWidget.setItem(i, x, temp(data[i - 1]['CONNECTOR']))
                        elif x == 4:
                            self.tableWidget.setItem(i, x, temp(data[i - 1]['Number of Fans']))
                        elif x == 5:
                            self.tableWidget.setItem(i, x, temp(data[i - 1]['HEATPIPES']))
                        elif x == 6:
                            self.tableWidget.setItem(i, x, temp(data[i - 1]['Score']))
                            self.tableWidget.item(i, x).setForeground(QtGui.QColor(255, 255, 255))

    def senddata(self):
        data = self.tableWidget.selectedItems()
        for item in data:
            print(item.text())
        setdata = "{} {}".format(data[1].text(), data[0].text())
        print(setdata)
        self.hide()
        self.ui = mainUi.mainwindow()
        mainUi.sinkname = str(setdata)
        self.ui.show()
        self.ui.lblsink.setText("{}".format(setdata))
        mainUi.sinkscore = data[6].text()
        print(mainUi.sinkscore)