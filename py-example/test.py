#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/19 14:40
# @Author : ChenShan
# Function :

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Form(QDialog):
    def __index__(self,parent = None):
        super().__init__(parent)

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()