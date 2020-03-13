from PyQt5 import QtCore,QtWidgets,QtGui,uic,QtWidgets
import connectdb
import databaseStructure
import mainUi


class historywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r'Ui\History.ui', self)
        self.setWindowTitle("PCbuildProject")
        self.setFixedSize(self.size())
        self.pushBack.clicked.connect(self.getBack)
        self.pushdelete.clicked.connect(self.deleterow)
        self.tableWidget.setColumnCount(9)
        self.showdata()

    def showdata(self):
        data = connectdb.getHistory()
        row = len(data)
        self.tableWidget.setRowCount(row)
        temp = QtWidgets.QTableWidgetItem
        self.tableWidget.setHorizontalHeaderItem(0, temp("PC"))
        self.tableWidget.setHorizontalHeaderItem(1, temp("CPU"))
        self.tableWidget.setHorizontalHeaderItem(2, temp("VGA"))
        self.tableWidget.setHorizontalHeaderItem(3, temp("RAM"))
        self.tableWidget.setHorizontalHeaderItem(4, temp("MB"))
        self.tableWidget.setHorizontalHeaderItem(5, temp("PSU"))
        self.tableWidget.setHorizontalHeaderItem(6, temp("Sink"))
        self.tableWidget.setHorizontalHeaderItem(7, temp("HDD1"))
        self.tableWidget.setHorizontalHeaderItem(8, temp("HDD2"))
        self.tableWidget.setHorizontalHeaderItem(9, temp("score"))
        for i in range(0, row):
            for x in range(10):
                if x == 0:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['PC']))
                elif x == 1:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['CPU']))
                elif x == 2:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['VGA']))
                elif x == 3:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['RAM']))
                elif x == 4:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['MB']))
                elif x == 5:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['PSU']))
                elif x == 6:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['Sink']))
                elif x == 7:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['HDD1']))
                elif x == 8:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['HDD2']))
                elif x == 9:
                    self.tableWidget.setItem(i, x, temp(data[i - 1]['score']))

    def getBack(self):
        self.hide()
        self.ui = mainUi.mainwindow()
        self.ui.show()

    def deleterow(self):
        data = self.tableWidget.selectedItems()
        todel = data[0].text()
        print(todel)
        print(type(todel))
        databaseStructure.delHistory(todel)
        self.showdata()
