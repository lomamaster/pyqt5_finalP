from PyQt5 import QtCore,QtWidgets,QtGui,uic,QtWidgets
from PyQt5.QtWidgets import QMessageBox

cpuscore = 1.00
gpuscore = 1.00
psuscore = 1.00
hddscore = 0.00
sinkscore = 1.00
ramscore = 1.00
mbscore = 1.00

PCname = ""
cpuname = ""
vganame = ""
mbname = ""
psuname = ""
hdd1name = ""
hdd2name = ""
sinkname = ""
ramname = ""

class mainwindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r'Ui\mainUi.ui', self)
        self.setWindowTitle("PCbuildProject")
        self.setFixedSize(self.size())
        self.selectCPU.clicked.connect(self.openCPU)
        self.selectMainboard.clicked.connect(self.openMB)
        self.selectHDD1.clicked.connect(self.openHDD1)
        self.selectHDD2.clicked.connect(self.openHDD2)
        self.selectRam.clicked.connect(self.openRAM)
        self.selectPSU.clicked.connect(self.openPSU)
        self.selectVGA.clicked.connect(self.openGPU)
        self.selectSink.clicked.connect(self.openSink)
        self.btnhistory.clicked.connect(self.openHistory)
        self.btncal.clicked.connect(self.openCal)
        self.lblcpu.setText(cpuname)
        self.lblmb.setText(mbname)
        self.lblhdd.setText(hdd1name)
        self.lblhdd_2.setText(hdd2name)
        self.lblram.setText(ramname)
        self.lblvga.setText(vganame)
        self.lblpsu.setText(psuname)
        self.lblsink.setText(sinkname)

    def openCPU(self):
        import selectCPU
        self.hide()
        self.Open = selectCPU.cpuwindow()
        self.Open.show()

    def openHDD1(self):
        import selectHDD
        self.hide()
        self.Open = selectHDD.hdd1window()
        self.Open.show()

    def openHDD2(self):
        import selectHDD2
        self.hide()
        self.Open = selectHDD2.hdd2window()
        self.Open.show()

    def openMB(self):
        import selectMB
        self.hide()
        self.Open = selectMB.mbwindow()
        self.Open.show()

    def openRAM(self):
        import selectRAM
        self.hide()
        self.Open = selectRAM.ramwindow()
        self.Open.show()

    def openPSU(self):
        import selectPSU
        self.hide()
        self.Open = selectPSU.psuwindow()
        self.Open.show()

    def openGPU(self):
        import selectGPU
        self.hide()
        self.Open = selectGPU.gpuwindow()
        self.Open.show()

    def openSink(self):
        import selectSink
        self.hide()
        self.Open = selectSink.sinkwindow()
        self.Open.show()

    def openHistory(self):
        import historyForm
        self.hide()
        self.Open = historyForm.historywindow()
        self.Open.show()

    def openCal(self):
        if self.lblcpu.text() == "" or self.lblvga.text() == "" or self.lblpsu.text() == "" or (self.lblhdd.text() == "" or self.lblhdd_2.text() == "") or self.lblmb.text() == "" \
                or self.lblsink.text() == "" or self.lblram.text() == "" or self.lineEdit.text() == "":
            self.erroroccurst()
        else:
            import calForm
            print(cpuscore)
            self.cpuscore = float(cpuscore)
            print(gpuscore)
            self.gpuscore = float(gpuscore)
            print(psuscore)
            self.psuscore = float(psuscore)
            print(hddscore)
            self.hddscore = float(hddscore)
            print(mbscore)
            self.mbscore = float(mbscore)
            print(sinkscore)
            self.sinkscore = float(sinkscore)
            print(ramscore)
            self.ramscore = float(ramscore)
            total = ((self.cpuscore + self.gpuscore + self.ramscore) * (self.mbscore + self.psuscore + self.sinkscore)) * (100 * self.hddscore)
            selectedcpu = self.lblcpu.text()
            selectedgpu = self.lblvga.text()
            selectedpsu = self.lblpsu.text()
            selectedhdd1 = self.lblhdd.text()
            selectedhdd2 = self.lblhdd_2.text()
            selectedmb = self.lblmb.text()
            selectedsink = self.lblsink.text()
            selectedram = self.lblram.text()
            thisPC = self.lineEdit.text()
            print(selectedcpu)
            print(total)
            self.Open = calForm.calculationwindow(thisPC, selectedcpu, selectedgpu, selectedpsu, selectedhdd1, selectedhdd2, selectedmb, selectedsink, selectedram, total)
            self.Open.show()

    def erroroccurst(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error.")
        msg.setText("Please Select Hardware")
        msg.setIcon(QMessageBox.Critical)

        x = msg.exec_()

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = mainwindow()
    window.show()
    window.raise_()
    sys.exit(app.exec())