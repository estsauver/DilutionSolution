#!python

__author__ = 'estsauver'

import sys

from PySide.QtGui import *



from ui_dilutionSolution import Ui_Dialog

def stock_calc(self, desVol, desVolUnits, desConc, desConcunits, stockConc, stockConcUnits):
    assert isinstance(stockConcUnits, float)
    assert isinstance(desConc, float)
    assert isinstance(desConcunits,float)
    assert isinstance(desVol,float)
    assert isinstance(desVolUnits,float)
    assert isinstance(stockConc,float)
    assert isinstance(stockConcUnits,float)
    desConcinMolar = desConc*desConcunits
    print "Deisred Concentration in Molar %s" %desConcinMolar
    desVolinL = desVol*desVolUnits
    print "Desired Volume in L: %s" %desVolinL
    stockConcinMolar = stockConc*stockConcUnits
    print "Stock Concentration in Molar %s" %stockConcinMolar
    stockVolumeinL = (desConcinMolar*desVolinL)/stockConcinMolar
    print "Stock Volume in Liters: %s" %stockVolumeinL
    soluteVolumeinL = desVolinL-stockVolumeinL
    print "Solute Volume in LIters: %s" %soluteVolumeinL
    assert (stockVolumeinL+soluteVolumeinL==desVolinL)
    return (stockVolumeinL,soluteVolumeinL)

class MainWindow(QMainWindow, Ui_Dialog):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)


    def accept(self):
        unitConcDict = {"Mol/L":1.0,"mMol/L":0.001,"mMol/mL":1.0,"mMol/uL":1000,"uMol/L":0.000001, "uMol/mL":0.001,
                        "uMol/uL":1.0,"nMol/L":0.000000001, "nMol/mL":0.000001, "nMol/uL":0.001, "nMol/nL":1.0,"nMol/pL":1000.0,
                        "pMol/L":0.000000000001,"pMol/mL":0.000000001, "pMol/uL":0.000001, "pMol/nL":0.001, "pMol/pL":1}
        unitVolDict = {"L":1.0,"mL":0.001,"uL":0.000001,"pL":0.000000001}
        desConc = float(self.desConcValue.text())
        desConcUnitsString = self.desConcUnits.currentItem().text()
        desConcUnits = unitConcDict[desConcUnitsString]

        desVol = float(self.desVolValue.text())
        desVolUnitsString = self.desVolUnits.currentItem().text()
        desVolUnits = unitVolDict[desVolUnitsString]

        stockConc = float(self.stockConcValue.text())
        stockConcUnitsString = self.stockConcUnits.currentItem().text()
        stockConcUnits = unitConcDict[stockConcUnitsString]

        print (desVol, desVolUnits, desConc, desConcUnits, stockConc, stockConcUnits)
        (stockVolinL, soluteVolinL) = stock_calc(super, desVol, desVolUnits, desConc, desConcUnits, stockConc, stockConcUnits)

        self.label_3.setText("L: %s " % unicode(stockVolinL))
        self.label_4.setText("mL: %s " % unicode(stockVolinL*1000.0))
        self.label_5.setText("uL: %s " % unicode(stockVolinL*1000000.0))
        self.label_6.setText("L: %s " % unicode(soluteVolinL))
        self.label_7.setText("ml: %s " %unicode(soluteVolinL*1000.0))
        self.label_8.setText("ul: %s " %unicode(soluteVolinL*1000000.0))






    def reject(self):
        QApplication.instance().quit()


if __name__=="__main__":
    app = QApplication(sys.argv)
    frame = MainWindow()
    frame.show()
    app.exec_()