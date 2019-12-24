#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/21 19:38
# @Author : ChenShan
# Function :
import os
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class SetPenColorDlg(QDialog):
    # 重载构造函数
    def __init__(self, parent=None):
        # 重载父类构造函数
        super().__init__(parent)
        # 改变窗口显示的title
        self.setWindowTitle("SetPenWidth")

        # red设置的Label
        self.RLabel = QLabel("Red :")
        # red的数字框
        self.RSpinBox = QDoubleSpinBox(self)
        # 范围
        self.RSpinBox.setRange(0, 255)
        # 初始值
        self.RSpinBox.setValue(255)

        # green设置的Label
        self.GLabel = QLabel("Green :")
        # green的数字框
        self.GSpinBox = QDoubleSpinBox(self)
        # 范围
        self.GSpinBox.setRange(0, 255)
        # 初始值
        self.GSpinBox.setValue(255)

        # blue设置的Label
        self.BLabel = QLabel("Blue :")
        # blue的数字框
        self.BSpinBox = QDoubleSpinBox(self)
        # 范围
        self.BSpinBox.setRange(0, 255)
        # 初始值
        self.BSpinBox.setValue(255)

        # Color Lable
        self.ColorLabel = QLabel("Color :")
        self.resultLabel = QLabel("255,255,255")

        # ok/cancel
        self.okButton = QPushButton("&OK")
        self.cancelButton = QPushButton("Cancel")

        # 显示，竖直布局
        self.layout = QGridLayout(self)

        self.layout.addWidget(self.RLabel, 0, 0)
        self.layout.addWidget(self.RSpinBox, 0, 1)

        self.layout.addWidget(self.GLabel, 1, 0)
        self.layout.addWidget(self.GSpinBox, 1, 1)

        self.layout.addWidget(self.BLabel, 2, 0)
        self.layout.addWidget(self.BSpinBox, 2, 1)

        self.layout.addWidget(self.okButton, 3, 0)
        self.layout.addWidget(self.cancelButton, 3, 1)

        self.okButton.clicked.connect(self.accept)
        self.cancelButton.clicked.connect(self.reject)


class SetPenWidthDlg(QDialog):
    # 重载构造函数
    def __init__(self, parent=None):
        # 重载父类构造函数
        super().__init__(parent)
        # 改变窗口显示的title
        self.setWindowTitle("SetPenWidth")

        # 设置width的Label
        self.widthLabel = QLabel("Width :")
        # width的数字框
        self.widthSpinBox = QDoubleSpinBox(self)
        # 范围
        self.widthSpinBox.setRange(1, 30)
        # 初始值
        self.widthSpinBox.setValue(3)

        # ok/cancel
        self.okButton = QPushButton("&OK")
        self.cancelButton = QPushButton("Cancel")

        # 显示，竖直布局
        self.layout = QGridLayout(self)

        self.layout.addWidget(self.widthLabel, 0, 0)
        self.layout.addWidget(self.widthSpinBox, 0, 1)
        self.layout.addWidget(self.okButton, 1, 0)
        self.layout.addWidget(self.cancelButton, 1, 1)

        self.okButton.clicked.connect(self.accept)
        self.cancelButton.clicked.connect(self.reject)


# 新建一个主窗口程序，继承自QMainWindow
class myMainWindow(QMainWindow):
    # 重载构造函数
    def __init__(self, parent=None):
        # 重载父类构造函数
        super().__init__(parent)
        # 改变窗口显示的title
        self.setWindowTitle("PaintBrush")

        # 加载数据
        self.initData()

        # 加载画板
        self.myLabel = QLabel()
        self.myPixmap = QPixmap(QSize(1000, 800))
        self.myPixmap.fill(Qt.white)
        self.myLabel.setPixmap(self.myPixmap)
        self.initView()

        # 动作组
        # 徒手画
        self.drawLineAction = QAction(QIcon("images/pen.png"), "&Draw.", self)
        self.drawLineAction.triggered.connect(self.drawLine)
        self.drawLineAction.setStatusTip("Draw.")

        # 设置颜色
        self.setColorAction = QAction(QIcon("images/color.png"), "&set color.", self)
        self.setColorAction.triggered.connect(self.setColor)
        self.setColorAction.setStatusTip("set color.")
        # 设置线宽
        self.setWidthAction = QAction(QIcon("images/width.png"), "&set width.", self)
        self.setWidthAction.triggered.connect(self.setWidth)
        self.setWidthAction.setStatusTip("set width.")
        # 打开文件
        self.fileOpenAction = QAction(QIcon("images/fileopen.png"), "&Open an image.", self)
        self.fileOpenAction.triggered.connect(self.openFile)
        self.fileOpenAction.setShortcut(QKeySequence.Open)
        self.fileOpenAction.setStatusTip("Open an image.")
        # 保存文件
        self.fileSaveAction = QAction(QIcon("images/filesave.png"), "&Save an image.", self)
        self.fileSaveAction.triggered.connect(self.saveFile)
        self.fileSaveAction.setShortcut(QKeySequence.Save)
        self.fileSaveAction.setStatusTip("Save an image.")

        # 清空
        self.ClearAction = QAction(QIcon("clear.png"), "new a paper.", self)
        self.ClearAction.triggered.connect(self.initView)
        self.ClearAction.setStatusTip("new a paper.")

        # 工具栏
        self.fileToolbar = self.addToolBar("File")

        self.fileToolbar.addAction(self.drawLineAction)
        self.fileToolbar.addAction(self.setColorAction)
        self.fileToolbar.addAction(self.setWidthAction)
        self.fileToolbar.addAction(self.fileOpenAction)
        self.fileToolbar.addAction(self.fileSaveAction)
        self.fileToolbar.addAction(self.ClearAction)

        # 状态栏
        # 定义一个Label用来显示鼠标位置的更新
        self.statusLabel = QLabel("Moun")
        # 改变状态栏的Style
        self.statusLabel.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
        # 定义一个状态栏对象
        self.status = self.statusBar()
        self.status.setSizeGripEnabled(False)
        # 用addPermanentWidget()在状态栏显示Label里的内容
        self.status.addPermanentWidget(self.statusLabel)
        # 在状态栏显示信息，后一个参数为显示时间（毫秒）
        self.status.showMessage("Ready", 5000)

    def initView(self):
        # 创建画板
        # 设置界面的尺寸为__size
        self.Clear()
        self.myLabel = QLabel()
        self.myPixmap = QPixmap(QSize(1000, 800))
        self.myPixmap.fill(Qt.white)
        self.myLabel.setPixmap(self.myPixmap)

        # 把图显示在中间
        self.setCentralWidget(self.myLabel)

    def drawLine(self):
        self.pos_start = QPoint(self.pos_start_X, self.pos_start_Y)
        self.pos_end = QPoint(self.pos_end_X, self.pos_end_Y)
        self.painter = QPainter(self.myPixmap)
        self.painter.setPen(QPen(QColor(self.red, self.green, self.blue), self.pen_width))
        self.painter.drawLine(self.pos_start, self.pos_end)
        self.myLabel.setPixmap(self.myPixmap)

    def setColor(self):
        self.dialog_color = SetPenColorDlg(self)
        # 初始化上次保存的颜色值
        self.dialog_color.RSpinBox.setValue(self.red)
        self.dialog_color.GSpinBox.setValue(self.green)
        self.dialog_color.BSpinBox.setValue(self.blue)
        if self.dialog_color.exec_():
            # 获取RSpinBox中更新的数据
            self.red = (int)(self.dialog_color.RSpinBox.value())
            # 获取GSpinBox中更新的数据
            self.green = (int)(self.dialog_color.GSpinBox.value())
            # 获取BComboBox中更新的数据
            self.blue = (int)(self.dialog_color.BSpinBox.value())
            # 把更新结果显示在resultLabel中
            self.dialog_color.resultLabel.setText("{},{},{}".format(self.red, self.green, self.blue))

    def setWidth(self):
        self.dialog_width = SetPenWidthDlg(self)
        # 初始化上次保存的颜色值
        self.dialog_width.widthSpinBox.setValue(self.pen_width)
        if self.dialog_width.exec_():
            self.pen_width = self.dialog_width.widthSpinBox.value()

    # 警告当前图像未保存
    def okToContinue(self):
        if self.dirty:
            reply = QMessageBox.question(self,
                                            "Image Changer - Unsaved Changes",
                                            "Save unsaved changes?",
                                            QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            if reply == QMessageBox.Cancel:
                return False
            elif reply == QMessageBox.Yes:
                return self.fileSaveAs()
        return True

    def openFile(self):
        if not self.okToContinue():
            return
        dir = (os.path.dirname(self.filename)
               if self.filename is not None else ".")
        formats = (["*.{}".format(format.data().decode("ascii").lower())
                    for format in QImageReader.supportedImageFormats()])
        fname = QFileDialog.getOpenFileName(self,
                                            "Image Changer - Choose Image", dir,
                                            "Image files ({})".format(" ".join(formats)))
        if fname:
            print(fname[0])
            self.loadFile(fname[0])
            self.updateFileMenu()

        # if not self.okToContinue():
        #     return
        # dir = (os.path.dirname(self.filename)
        #        if self.filename is not None else ".")
        # formats = (["*.{}".format(format.data().decode("ascii").lower())
        #             for format in QImageReader.supportedImageFormats()])
        # fname = QFileDialog.getOpenFileName(self,
        #                                     "Image Changer - Choose Image", dir,
        #                                     "Image files ({})".format(" ".join(formats)))
        #
        # if fname:
        #     print(fname[0])
        #     self.loadFile(fname[0])
        #     print('okay')
        #     # self.painter = QPainter(self.pixmap)
        #     # self.painter.setPen(self.pen)
        #     # self.updateFileMenu()
        #     print(self.filename)
        #     self.updatePainter()
        #     print(type(self.filename))

    def saveFile(self):
        savePath = QFileDialog.getSaveFileName(self, 'Save Your Paint', '.\\', '*.png')
        print(savePath)
        if savePath[0] == "":
            print("Save cancel")
            return
        image = self.pixmap
        print("save...")
        image.save(savePath[0])
        self.updateStatus("Saved as {}".format(savePath))

        # if self.image.isNull():
        #     return True
        # fname = self.filename if self.filename is not None else "."
        # formats = (["*.{}".format(format.data().decode("ascii").lower())
        #             for format in QImageWriter.supportedImageFormats()])
        # fname = QFileDialog.getSaveFileName(self,
        #                                        "Image Changer - Save Image", fname,
        #                                        "Image files ({})".format(" ".join(formats)))
        # fname = fname[0]
        # if fname:
        #     print(fname)
        #     if "." not in fname:
        #         fname += ".png"
        #     self.addRecentFile(fname)
        #     self.filename = fname
        #
        #     if self.image.save(self.filename, None):
        #         self.updateStatus("Saved as {}".format(self.filename))
        #         self.dirty = False
        #         return True
        #     else:
        #         self.updateStatus("Failed to save {}".format(
        #             self.filename))
        #         return False
        # return False

    def loadFile(self, fname=None):
        if fname is None:
            action = self.sender()
            if isinstance(action, QAction):
                fname = action.data()
                if not self.okToContinue():
                    return
            else:
                return
        if fname:
            self.filename = None
            image = QImage(fname)
            if image.isNull():
                message = "Failed to read {}".format(fname)
            else:
                self.addRecentFile(fname)
                self.image = QImage()
                self.image = image
                self.filename = fname
                self.showImage()
                self.dirty = False
                message = "Loaded {}".format(os.path.basename(fname))
            self.updateStatus(message)

    def addRecentFile(self, fname):
        if fname is None:
            return
        if fname not in self.recentFiles:
            if len(self.recentFiles) < 10:
                self.recentFiles = [fname] + self.recentFiles
            else:
                self.recentFiles = [fname] + self.recentFiles[:8]
                print(len(self.recentFiles))

    def updateFileMenu(self):
        self.fileMenu.clear()
        self.fileMenu.addAction(self.fileOpenAction)
        self.fileMenu.addAction(self.fileSaveAction)
        current = self.filename
        recentFiles = []
        print(self.recentFiles)
        for fname in self.recentFiles:
            if fname != current and QFile.exists(fname):
                recentFiles.append(fname)
        if recentFiles:
            self.fileMenu.addSeparator()
            for i, fname in enumerate(recentFiles):
                action = QAction(QIcon("images/icon.png"),
                                    "&{} {}".format(i + 1, QFileInfo(
                                        fname).fileName()), self)
                action.setData(fname)
                action.triggered.connect(lambda: self.loadFile(fname))
                self.fileMenu.addAction(action)

    def Clear(self):
        # 清空画板
        self.myPixmap.fill(Qt.white)
        self.update()
        self.dirty = False

    def initData(self):
        # 参数
        self.pos_start_X = 0
        self.pos_start_Y = 0
        self.pos_end_X = 0
        self.pos_end_Y = 0
        self.red = 0
        self.green = 0
        self.blue = 255
        self.pen_width = 3
        self.dirty = False
        self.filename = None
        self.recentFiles = []
        # self.image = QImage()

    def mousePressEvent(self, event):
        print("startx=", self.pos_start_X, " starty=", self.pos_start_Y)
        self.pos_start = event.pos()
        self.pos_start_X = event.pos().x()
        self.pos_start_Y = event.pos().y()

    def mouseMoveEvent(self, event):
        self.pos_end_X = event.pos().x()
        self.pos_end_Y = event.pos().y()
        self.drawLine()
        self.pos_start_X = event.pos().x()
        self.pos_start_Y = event.pos().y()

    def mouseReleaseEvent(self, event):
        print("endx=", self.pos_end_X, " endy=", self.pos_end_Y)
        self.pos_end_X = event.pos().x()
        self.pos_end_Y = event.pos().y()
        self.drawLine()

    def showImage(self, percent=None):
        if self.image.isNull():
            return

        self.myLabel.setPixmap(QPixmap.fromImage(self.image))


app = QApplication(sys.argv)
form = myMainWindow()
# 设定最小的程序窗口大小
form.setMinimumSize(800, 800)
form.show()
app.exec_()
