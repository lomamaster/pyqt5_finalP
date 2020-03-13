from PyQt5 import QtCore,QtWidgets,QtGui,uic,QtWidgets

import connectdb
import mainUi

class gpuwindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi(r'Ui\SelectGPU.ui', self)
        self.setWindowTitle("PCbuildProject")
        self.setFixedSize(self.size())
        self.addSelected.clicked.connect(self.senddata)
        self.pushreset.clicked.connect(self.reset_pressed)
        self.tableWidget.setColumnCount(10)
        temp = QtWidgets.QTableWidgetItem

        series = connectdb.onlySeries()
        for i in series:
            self.comboBox.addItem(i)
        self.showData()
        self.comboBox.currentIndexChanged.connect(self.selectedData)
        self.pushBack.clicked.connect(self.getBack)

    def showData(self):
        # self.currentTextChanged.connect(self.selectedtype)
        data = connectdb.getVGAdata()
        print("pulled data gpu")
        row = len(data)
        print("set data")
        # self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(row)
        print("set row")
        temp = QtWidgets.QTableWidgetItem
        print("set temp")
        self.tableWidget.setHorizontalHeaderItem(0, temp("Name"))
        self.tableWidget.setHorizontalHeaderItem(1, temp("VRAM"))
        self.tableWidget.setHorizontalHeaderItem(2, temp("GDDR"))
        self.tableWidget.setHorizontalHeaderItem(3, temp("SPC"))
        self.tableWidget.setHorizontalHeaderItem(4, temp("PowerRequirment"))
        self.tableWidget.setHorizontalHeaderItem(5, temp("ShaderCore"))
        self.tableWidget.setHorizontalHeaderItem(6, temp("Core speed"))
        self.tableWidget.setHorizontalHeaderItem(7, temp("Memory Bus"))
        self.tableWidget.setHorizontalHeaderItem(8, temp("Series"))
        self.tableWidget.setHorizontalHeaderItem(9, temp("  "))
        print("set header")
        for i in range(0, row):
            for x in range(10):
                if x == 0:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['Name']))
                elif x == 1:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['VRAM']))
                elif x == 2:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['GDDR']))
                elif x == 3:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['SPC']))
                elif x == 4:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['PowerRequirment']))
                elif x == 5:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['ShaderCore']))
                elif x == 6:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['Core speed']))
                elif x == 7:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['Memory Bus']))
                elif x == 8:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['Series']))
                elif x == 9:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['Score']))
                    self.tableWidget.item(i, x).setForeground(QtGui.QColor(255, 255, 255))

    def reset_pressed(self):
        self.showData()

    def selectedData(self):
        selected = str(self.comboBox.currentText())
        print(selected)
        print(type(selected))
        # self.currentTextChanged.connect(self.selectedtype)
        data = connectdb.getselectSeriesVGAdata(selected)
        print("pulled data gpu")
        row = len(data)
        print("set data")
        # self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(row)
        print("set row")
        temp = QtWidgets.QTableWidgetItem
        print("set temp")
        self.tableWidget.setHorizontalHeaderItem(0, temp("Name"))
        self.tableWidget.setHorizontalHeaderItem(1, temp("VRAM"))
        self.tableWidget.setHorizontalHeaderItem(2, temp("GDDR"))
        self.tableWidget.setHorizontalHeaderItem(3, temp("SPC"))
        self.tableWidget.setHorizontalHeaderItem(4, temp("PowerRequirment"))
        self.tableWidget.setHorizontalHeaderItem(5, temp("ShaderCore"))
        self.tableWidget.setHorizontalHeaderItem(6, temp("Core speed"))
        self.tableWidget.setHorizontalHeaderItem(7, temp("Memory Bus"))
        self.tableWidget.setHorizontalHeaderItem(8, temp("Series"))
        self.tableWidget.setHorizontalHeaderItem(9, temp("  "))
        print("set header")
        for i in range(0, row):
            for x in range(10):
                if x == 0:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['Name']))
                elif x == 1:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['VRAM']))
                elif x == 2:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['GDDR']))
                elif x == 3:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['SPC']))
                elif x == 4:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['PowerRequirment']))
                elif x == 5:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['ShaderCore']))
                elif x == 6:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['Core speed']))
                elif x == 7:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['Memory Bus']))
                elif x == 8:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['Series']))
                elif x == 9:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['Score']))
                    self.tableWidget.item(i, x).setForeground(QtGui.QColor(255, 255, 255))


    def senddata(self):
        data = self.tableWidget.selectedItems()
        for item in data:
            print(item.text())
        setdata = "{}".format(data[0].text())
        print(setdata)
        self.hide()
        self.ui = mainUi.mainwindow()
        mainUi.vganame = str(setdata)
        self.ui.show()
        self.ui.lblvga.setText("{}".format(setdata))
        mainUi.gpuscore = data[9].text()
        print(mainUi.gpuscore)

    def getBack(self):
        self.hide()
        self.ui = mainUi.mainwindow()
        self.ui.show()