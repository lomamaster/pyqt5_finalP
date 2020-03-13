from PyQt5 import QtCore,QtWidgets,QtGui,uic,QtWidgets

import databaseStructure
import mainUi
class calculationwindow(QtWidgets.QMainWindow):
    def __init__(self,thispc,selectedcpu,selectedgpu,selectedpsu,selectedhdd1,selectedhdd2,selectedmb,selectedsink,selectedram,total):
        super().__init__()
        uic.loadUi(r'Ui\CalUi.ui', self)
        self.setWindowTitle("PCbuildProject")
        self.setFixedSize(self.size())
        self.thispc.setText("{}".format(thispc))
        self.cpu.setText("{}".format(selectedcpu))
        self.gpu.setText("{}".format(selectedgpu))
        self.mb.setText("{}".format(selectedmb))
        self.ram.setText("{}".format(selectedram))
        self.hdd1.setText("{}".format(selectedhdd1))
        self.hdd2.setText("{}".format(selectedhdd2))
        self.sink.setText("{}".format(selectedsink))
        self.psu.setText("{}".format(selectedpsu))
        self.score.setText("{}".format(total))
        self.pushButton.clicked.connect(self.addtohistory)
        self.pushButton_2.clicked.connect(self.getBack)

    def addtohistory(self):
        thispc = self.thispc.text()
        selectedcpu = self.cpu.text()
        selectedgpu = self.gpu.text()
        selectedpsu = self.psu.text()
        selectedhdd1 = self.hdd1.text()
        selectedhdd2 = self.hdd2.text()
        selectedmb = self.mb.text()
        selectedsink = self.sink.text()
        selectedram = self.ram.text()
        total = self.score.text()
        print(selectedcpu)
        print(selectedgpu)
        databaseStructure.addHistory(thispc,selectedcpu,selectedgpu,selectedpsu,selectedhdd1,selectedhdd2,selectedmb,selectedsink,selectedram,total)
        self.hide()
        print("recorded")
    def getBack(self):
        self.hide()
        self.ui = mainUi.mainwindow()
        self.ui.show()