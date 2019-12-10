import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import aaa

class myDlg(QDialog,aaa.Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        

app = QApplication(sys.argv)
form = myDlg()
form.show()
app.exec_()
