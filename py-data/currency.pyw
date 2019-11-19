import sys
import urllib.request
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Form(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        date = self.getdata()
        rates = sorted(self.rates.keys())

        dateLabel = QLabel(date)
        self.fromComboBox = QComboBox()
        self.fromComboBox.addItems(rates)
        self.fromSpinBox = QDoubleSpinBox()
        self.fromSpinBox.setRange(0.01, 10000000.00)
        self.fromSpinBox.setValue(1.00)
        self.toComboBox = QComboBox()
        self.toComboBox.addItems(rates)
        self.toLabel = QLabel("1.00")
        grid = QGridLayout()
        grid.addWidget(dateLabel, 0, 0)
        grid.addWidget(self.fromComboBox, 1, 0)
        grid.addWidget(self.fromSpinBox, 1, 1)
        grid.addWidget(self.toComboBox, 2, 0)
        grid.addWidget(self.toLabel, 2, 1)
        self.setLayout(grid)
        self.fromComboBox.currentIndexChanged.connect(self.updateUi)
        self.toComboBox.currentIndexChanged.connect(self.updateUi)
        self.fromSpinBox.valueChanged.connect(self.updateUi)
        self.setWindowTitle("Currency")
        
    def updateUi(self):
        to = self.toComboBox.currentText()
        from_ = self.fromComboBox.currentText()
        amount = ((self.rates[to]/self.rates[from_])*self.fromSpinBox.value())
        self.toLabel.setText("{0:.2f}".format(amount))
        
    def getdata(self): 
        self.rates = {}
        try:
            date = "Unknown"
            data = urllib.request.urlopen("https://www.gov.uk"
                  "/government/uploads/system/uploads"
                  "/attachment_data/file/702273"
                  "/exrates-monthly-0518.csv").read()
            for line in data.decode("utf-8", "replace").split("\n"):
                line = line.rstrip()
                if not line or line.startswith(("#", "Closing ", "Country")):
                    continue
                fields = line.split(",")
                if line.startswith("China"):
                    date = fields[-1]
                else:
                    try:
                        value = float(fields[3])
                        self.rates[fields[0]] = value
                    except ValueError:
                        pass
            return "Exchange Rates Date: " + date
        except Exception as e:
            return "Failed to download:\n{}".format(e)

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()

