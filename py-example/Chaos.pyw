import os
import platform
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import numpy as np
import matplotlib
matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure #注意不是pyplot下的那个figure


class myMainWindow(QMainWindow):
      def __init__(self, parent=None):
            super().__init__(parent)
            self.setWindowTitle("Logistic Map: x:=rx(1-x)")

            #添加工具栏
            self.labelX = QLabel('x1: ')
            self.labelR = QLabel('    r: ')
            self.spinX = QDoubleSpinBox()
            self.spinX.setRange(0, 1)
            self.spinX.setValue(0.02)
            self.spinX.setSingleStep(0.01)
            self.spinR = QDoubleSpinBox()
            self.spinR.setRange(1.0, 6.0)
            self.spinR.setValue(2.0)
            self.spinR.setSingleStep(0.02)
            
            s = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.layout = QHBoxLayout()
            self.layout.addWidget(self.labelX)
            self.layout.addWidget(self.spinX)
            self.layout.addWidget(self.labelR)
            self.layout.addWidget(self.spinR)
            self.layout.addSpacerItem(s)
            
            self.containWidget = QWidget()
            self.containWidget.setLayout(self.layout)
            self.toolDockWidget = QDockWidget("Input:", self)
            self.toolDockWidget.setAllowedAreas(Qt.BottomDockWidgetArea)
            self.toolDockWidget.setWidget(self.containWidget)
            self.addDockWidget(Qt.BottomDockWidgetArea, self.toolDockWidget)

            self.spinX.valueChanged.connect(self.updateUi)
            self.spinR.valueChanged.connect(self.updateUi)

            #绘图
            self.fig = Figure(figsize=(12, 6), dpi=100)
            self.figureCanvas = FigureCanvas(self.fig)
            self.graphicscene = QGraphicsScene()
            self.graphicscene.addWidget(self.figureCanvas)
            self.graphicview = QGraphicsView()
            self.graphicview.setScene(self.graphicscene)
            self.setCentralWidget(self.graphicview)
            self.updateUi()
            
      def generateData(self, x1, r):
            arr = [x1]
            x = x1
            for i in range(1, 99):
                  x = r * x * (1-x)
                  arr.append(x)
            d = np.array(arr)
            return d

      def updateUi(self):
            #计算
            self.x1 = self.spinX.value()
            self.r = self.spinR.value()
            self.data = self.generateData(self.x1, self.r)

            #显示
            self.fig.clf()
            self.ax = self.fig.add_subplot(1,1,1)
            self.ax.plot(self.data)
            self.figureCanvas.draw()
                  
app = QApplication(sys.argv)
form = myMainWindow()
form.setMinimumSize(1500, 800)
form.show()
app.exec_()
