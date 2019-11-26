#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/26 10:40
# @Author : ChenShan
# Function : Using PyQt5 interface to calculate compound interest

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Form(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.principal = QLabel("Principal :")
        self.pDoubleBox = QDoubleSpinBox()
        self.pDoubleBox.setRange(1000.00, 1000000.00)
        self.pDoubleBox.setValue(10000.00)
        self.pDoubleBox.setPrefix("$ ")

        self.rate = QLabel("Rate :")
        self.rDoubleBox = QDoubleSpinBox()
        self.rDoubleBox.setRange(0.00, 60.00)
        self.rDoubleBox.setValue(5.00)
        self.rDoubleBox.setSuffix(" %")

        self.year = QLabel("Years :")
        self.timeComboBox = QComboBox()
        self.timeComboBox.addItems(["1 year", "2 years", "5 years", "10 years", "20 years"])

        self.amount = QLabel("Amount :")
        self.res = QLabel("$   10050")

        grid = QGridLayout()
        grid.addWidget(self.principal, 0, 0)
        grid.addWidget(self.pDoubleBox, 0, 1)
        grid.addWidget(self.rate, 1, 0)
        grid.addWidget(self.rDoubleBox, 1, 1)
        grid.addWidget(self.year, 2, 0)
        grid.addWidget(self.timeComboBox, 2, 1)
        grid.addWidget(self.amount, 3, 0)
        grid.addWidget(self.res, 3, 1)
        self.setLayout(grid)

        self.pDoubleBox.valueChanged.connect(self.updateUi)
        self.rDoubleBox.valueChanged.connect(self.updateUi)
        self.timeComboBox.currentIndexChanged.connect(self.updateUi)
        self.setWindowTitle("HOMEWORK-11 Interest")

    def updateUi(self):
        p = self.pDoubleBox.value()
        r = self.rDoubleBox.value()/100
        y = self.timeComboBox.currentText()
        # print(p)
        # print(r)
        # print(y)
        if y == "1 year":
            y = 1
        elif y == "2 years":
            y = 2
        elif y == "5 years":
            y = 5
        elif y == "10 years":
            y = 10
        elif y == "20 years":
            y = 20
        for i in range(0,y):
            ans = p+p*r
            p = ans
        self.res.setText("$   {0:.2f}".format(ans))

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()

