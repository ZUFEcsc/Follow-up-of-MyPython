#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/3 14:22
# @Author : ChenShan
# Function :
import os
import platform
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# 调画笔宽度的对话框
class PenWidthDlg(QDialog):
    def __init__(self, parent=None):
        super(PenWidthDlg, self).__init__(parent)

        widthLabel = QLabel("宽度:")
        self.widthSpinBox = QSpinBox()
        widthLabel.setBuddy(self.widthSpinBox)
        self.widthSpinBox.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.widthSpinBox.setRange(0, 50)

        okButton = QPushButton("ok")
        cancelButton = QPushButton("cancle")

        layout = QGridLayout()
        layout.addWidget(widthLabel, 0, 0)
        layout.addWidget(self.widthSpinBox, 0, 1)
        layout.addWidget(okButton, 1, 0)
        layout.addWidget(cancelButton, 1, 1)
        self.setLayout(layout)
        self.setWindowTitle("宽度设置")

        okButton.clicked.connect(self.accept)
        cancelButton.clicked.connect(self.reject)


class myMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # 初始化参数
        self.initData()
        # 清空画布
        self.initView()

        '''
        a="F:/ProgramData/我的python/python_programming/cat.jpg"
        self.pixmap = QPixmap(a)
        self.painter = QPainter(self.pixmap)
        self.painter.setPen(self.pen)
        self.imageLabel.setPixmap(self.pixmap)
        '''

        # 菜单栏
        self.Menu = self.menuBar().addMenu("菜单")

        # 清空
        self.ClearAction = QAction(QIcon("images/file-new.gif"), "清空", self)
        self.ClearAction.triggered.connect(self.initView)
        self.Menu.addAction(self.ClearAction)

        # 调画笔颜色
        self.changeColor = QAction(QIcon("images/color.png"), "颜色", self)
        self.changeColor.triggered.connect(self.showColorDialog)
        self.Menu.addAction(self.changeColor)

        # 调画笔粗细
        self.changeWidth = QAction(QIcon("images/width.ico"), "宽度", self)
        self.changeWidth.triggered.connect(self.showWidthDialog)
        self.Menu.addAction(self.changeWidth)

        '''
        #右侧停靠窗口
        logDockWidget = QDockWidget("Log", self)
        logDockWidget.setAllowedAreas(Qt.LeftDockWidgetArea|Qt.RightDockWidgetArea)
        self.listWidget = QListWidget()
        logDockWidget.setWidget(self.listWidget)
        self.addDockWidget(Qt.RightDockWidgetArea, logDockWidget)
        '''

        # 各种动作
        self.fileOpenAction = QAction(QIcon("images/fileopen.png"), "&Open", self)
        self.fileOpenAction.setShortcut(QKeySequence.Open)
        self.fileOpenAction.setToolTip("Open an image.")
        self.fileOpenAction.setStatusTip("Open an image.")
        self.fileOpenAction.triggered.connect(self.fileOpen)

        self.fileSaveAction = QAction(QIcon("images/filesave.png"), "&Save", self)
        self.fileSaveAction.setShortcut(QKeySequence.Save)
        self.fileSaveAction.setToolTip("Save an image.")
        self.fileSaveAction.setStatusTip("Save an image.")
        self.fileSaveAction.triggered.connect(self.fileSaveAs)

        # 工具栏
        fileToolbar = self.addToolBar("文件")
        fileToolbar.addAction(self.fileOpenAction)
        fileToolbar.addAction(self.fileSaveAction)

        editToolbar = self.addToolBar("清空")
        editToolbar.addAction(self.ClearAction)

        colorToolbar = self.addToolBar("颜色")
        colorToolbar.addAction(self.changeColor)

        widthToolbar = self.addToolBar("宽度")
        widthToolbar.addAction(self.changeWidth)

        # 状态栏
        self.sizeLabel = QLabel()
        self.sizeLabel.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
        status = self.statusBar()
        status.setSizeGripEnabled(False)
        status.addPermanentWidget(self.sizeLabel)
        status.showMessage("Ready", 5000)

    def initData(self):
        self.size = QSize(480, 460)
        self.pixmap = QPixmap(self.size)

        self.dirty = False
        self.filename = None
        self.recentFiles = []

        # 新建画笔
        self.width = 5
        self.color = QColor(0, 0, 0)
        self.pen = QPen()  # 实例化画笔对象
        self.pen.setColor(self.color)  # 设置画笔颜色
        self.pen = QPen(Qt.SolidLine)  # 实例化画笔对象.参数：画笔样式
        self.pen.setWidth(self.width)  # 设置画笔粗细

        # 新建绘图工具
        self.painter = QPainter(self.pixmap)
        self.painter.setPen(self.pen)

        # 鼠标位置
        self.__lastPos = QPoint(0, 0)  # 上一次鼠标位置
        self.__currentPos = QPoint(0, 0)  # 当前的鼠标位置

        self.image = QImage()

    def initView(self):
        # 设置界面的尺寸为__size
        self.Clear()
        self.imageLabel = QLabel()
        self.imageLabel.setPixmap(self.pixmap)
        self.setCentralWidget(self.imageLabel)

    def Clear(self):
        # 清空画板
        self.pixmap.fill(Qt.white)
        self.update()
        self.dirty = False

    def mousePressEvent(self, event):
        # 鼠标按下时，获取鼠标的当前位置保存为上一次位置
        self.__currentPos = event.pos()
        self.__lastPos = self.__currentPos

    def mouseMoveEvent(self, event):
        # 鼠标移动时，更新当前位置，并在上一个位置和当前位置间画线
        self.__currentPos = event.pos()
        # self.painter = QPainter(self.pixmap)
        # self.painter.setPen(self.pen)
        self.painter.drawLine(self.__lastPos, self.__currentPos)
        self.__lastPos = self.__currentPos
        self.imageLabel.setPixmap(self.pixmap)

    # 调画笔颜色
    def showColorDialog(self):
        col = QColorDialog.getColor()
        self.pen.setColor(col)
        self.painter.setPen(self.pen)

    def updateWidth(self):
        print(self.width)
        self.pen.setWidth(self.width)
        self.painter.setPen(self.pen)

    def showWidthDialog(self):
        dialog = PenWidthDlg(self)
        dialog.widthSpinBox.setValue(self.width)
        if dialog.exec_():
            self.width = dialog.widthSpinBox.value()
            self.updateWidth()

    def okToContinue(self):  # 警告当前图像未保存
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

    def fileOpen(self):
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
            self.loadFile(fname[0])
            print(self.filename)
            self.updatePainter()
            print(type(self.filename))

    def updatePainter(self):
        print(self.pixmap)
        '''
        try:
            self.painter = QPainter(self.pixmap)
        except Exception e:  
            print(Exception,":",e)
            '''
        print(444)
        self.painter.setPen(self.pen)
        print(555)
        self.imageLabel.setPixmap(self.pixmap)
        print(666)

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

    def updateStatus(self, message):
        self.statusBar().showMessage(message, 5000)
        if self.filename:
            self.setWindowTitle("Image Changer - {}[*]".format(
                os.path.basename(self.filename)))
            print(8)
        elif not self.image.isNull():
            self.setWindowTitle("Image Changer - Unnamed[*]")
        else:
            self.setWindowTitle("Image Changer[*]")

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

    def addRecentFile(self, fname):
        if fname is None:
            return
        if fname not in self.recentFiles:
            if len(self.recentFiles) < 10:
                self.recentFiles = [fname] + self.recentFiles
            else:
                self.recentFiles = [fname] + self.recentFiles[:8]
                print(len(self.recentFiles))

    def fileSaveAs(self):
        if self.image.isNull():
            return True
        fname = self.filename if self.filename is not None else "."
        formats = (["*.{}".format(format.data().decode("ascii").lower())
                    for format in QImageWriter.supportedImageFormats()])
        fname = QFileDialog.getSaveFileName(self,
                                            "Image Changer - Save Image", fname,
                                            "Image files ({})".format(" ".join(formats)))
        fname = fname[0]
        if fname:
            print(fname)
            if "." not in fname:
                fname += ".png"
            self.addRecentFile(fname)
            self.filename = fname

            if self.image.save(self.filename, None):
                self.updateStatus("Saved as {}".format(self.filename))
                self.dirty = False
                return True
            else:
                self.updateStatus("Failed to save {}".format(
                    self.filename))
                return False
        return False

    def showImage(self, percent=None):
        if self.image.isNull():
            return
        self.pixmap = QPixmap.fromImage(self.image)
        self.imageLabel.setPixmap(self.pixmap)


app = QApplication(sys.argv)
form = myMainWindow()
form.setMinimumSize(400, 400)
form.show()
app.exec_()