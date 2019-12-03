#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/3 10:59
# @Author : ChenShan
# Function :

import os
import platform
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class myMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.image = QImage()
        self.dirty = False
        self.filename = None
        self.mirroredvertically = False
        self.mirroredhorizontally = False

        # 图像
        self.pix = QPixmap()
        self.lastPoint = QPoint()
        self.endPoint = QPoint()
        # self.imageLabel.setAlignment(Qt.AlignCenter)
        # self.imageLabel.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.setCentralWidget(self.pix)

        # 右侧停靠窗口
        logDockWidget = QDockWidget("Log", self)
        logDockWidget.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        PenDockWidget = QDockWidget("Pen-set", self)
        PenDockWidget.setAllowedAreas(Qt.RightDockWidgetArea)

        self.listWidget = QListWidget()
        logDockWidget.setWidget(self.listWidget)

        widthLabel = QLabel("&Width:")
        self.widthSpinBox = QSpinBox()
        widthLabel.setBuddy(self.widthSpinBox)
        self.widthSpinBox.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.widthSpinBox.setRange(0, 24)
        self.beveledCheckBox = QCheckBox("&Beveled edges")
        styleLabel = QLabel("&Style:")
        self.styleComboBox = QComboBox()
        styleLabel.setBuddy(self.styleComboBox)
        self.styleComboBox.addItems(["Solid", "Dashed", "Dotted", "DashDotted", "DashDotDotted"])
        self.colorButton = QPushButton("Pen-color")

        self.penWidget = QWidget()
        buttonLayout = QHBoxLayout()
        buttonLayout.addStretch()
        layout = QGridLayout()
        layout.addWidget(widthLabel, 0, 0)
        layout.addWidget(self.widthSpinBox, 0, 1)
        layout.addWidget(self.beveledCheckBox, 0, 2)
        layout.addWidget(styleLabel, 1, 0)
        layout.addWidget(self.styleComboBox, 1, 1, 1, 2)
        layout.addWidget(self.colorButton, 2, 0, 1, 3)
        self.penWidget.setLayout(layout)

        # self.colorButton.clicked.connect(self.funColor())

        PenDockWidget.setWidget(self.penWidget)

        self.addDockWidget(Qt.RightDockWidgetArea, PenDockWidget)
        self.addDockWidget(Qt.RightDockWidgetArea, logDockWidget)

        # 状态栏
        self.sizeLabel = QLabel()
        self.sizeLabel.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
        status = self.statusBar()
        status.setSizeGripEnabled(False)
        status.addPermanentWidget(self.sizeLabel)
        status.showMessage("Ready", 5000)

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

        self.editUnMirrorAction = QAction(QIcon("images/editunmirror.png"), "&Unmirror", self)
        self.editUnMirrorAction.setShortcut("Ctrl+U")
        self.editUnMirrorAction.setToolTip("Unmirror the image")
        self.editUnMirrorAction.setStatusTip("Unmirror the image")
        self.editUnMirrorAction.setCheckable(True)
        self.editUnMirrorAction.setChecked(True)
        self.editUnMirrorAction.toggled.connect(self.editUnMirror)

        editMirrorHorizontalAction = QAction(QIcon("images/editmirrorhoriz.png"), "Mirror &Horizontally", self)
        editMirrorHorizontalAction.setShortcut("Ctrl+H")
        editMirrorHorizontalAction.setToolTip("Horizontally mirror the image")
        editMirrorHorizontalAction.setStatusTip("Horizontally mirror the image")
        editMirrorHorizontalAction.setCheckable(True)
        editMirrorHorizontalAction.toggled.connect(self.editMirrorHorizontal)

        editMirrorVerticalAction = QAction(QIcon("images/editmirrorvert.png"), "Mirror &Vertically", self)
        editMirrorVerticalAction.setShortcut("Ctrl+V")
        editMirrorVerticalAction.setToolTip("Vertically mirror the image")
        editMirrorVerticalAction.setStatusTip("Vertically mirror the image")
        editMirrorVerticalAction.setCheckable(True)
        editMirrorVerticalAction.toggled.connect(self.editMirrorVertical)

        mirrorGroup = QActionGroup(self)
        mirrorGroup.addAction(self.editUnMirrorAction)
        mirrorGroup.addAction(editMirrorHorizontalAction)
        mirrorGroup.addAction(editMirrorVerticalAction)

        # 菜单栏
        self.fileMenu = self.menuBar().addMenu("&File")
        self.fileMenu.addAction(self.fileOpenAction)
        self.fileMenu.addAction(self.fileSaveAction)

        editMenu = self.menuBar().addMenu("&Edit")
        editMenu.addAction(self.editUnMirrorAction)
        editMenu.addAction(editMirrorHorizontalAction)
        editMenu.addAction(editMirrorVerticalAction)

        # 工具栏
        fileToolbar = self.addToolBar("File")
        fileToolbar.addAction(self.fileOpenAction)
        fileToolbar.addAction(self.fileSaveAction)

        editToolbar = self.addToolBar("Edit")
        editToolbar.addAction(self.editUnMirrorAction)
        editToolbar.addAction(editMirrorHorizontalAction)
        editToolbar.addAction(editMirrorVerticalAction)

        self.recentFiles = []
        self.setWindowTitle("Image Changer")
    def  funColor(self):
        col = QColorDialog.getColor()

    # 重绘的复写函数 主要在这里绘制
    def paintEvent(self, event):
        pp = QPainter(self.pix)

        pen = QPen()  # 定义笔格式对象
        pen.setWidth(10)  # 设置笔的宽度
        pp.setPen(pen)  # 将笔格式赋值给 画笔

        # 根据鼠标指针前后两个位置绘制直线
        pp.drawLine(self.lastPoint, self.endPoint)
        # 让前一个坐标值等于后一个坐标值，
        # 这样就能实现画出连续的线
        self.lastPoint = self.endPoint
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix)  # 在画布上画出

    # 鼠标按压事件
    def mousePressEvent(self, event):
        # 鼠标左键按下
        if event.button() == Qt.LeftButton:
            self.lastPoint = event.pos()
            self.endPoint = self.lastPoint

    # 鼠标移动事件
    def mouseMoveEvent(self, event):
        # 鼠标左键按下的同时移动鼠标
        if event.buttons() and Qt.LeftButton:
            self.endPoint = event.pos()
            # 进行重新绘制
            self.update()

    # 鼠标释放事件
    def mouseReleaseEvent(self, event):
        # 鼠标左键释放
        if event.button() == Qt.LeftButton:
            self.endPoint = event.pos()
            # 进行重新绘制
            self.update()


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
            print(fname[0])
            self.loadFile(fname[0])
            self.updateFileMenu()

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
                self.editUnMirrorAction.setChecked(True)
                self.image = image
                self.filename = fname
                self.showImage()
                self.dirty = False
                self.sizeLabel.setText("{} x {}".format(
                    image.width(), image.height()))
                message = "Loaded {}".format(os.path.basename(fname))
            self.updateStatus(message)

    def updateStatus(self, message):
        self.statusBar().showMessage(message, 5000)
        self.listWidget.addItem(message)
        if self.filename:
            self.setWindowTitle("Image Changer - {}[*]".format(
                os.path.basename(self.filename)))
        elif not self.image.isNull():
            self.setWindowTitle("Image Changer - Unnamed[*]")
        else:
            self.setWindowTitle("Image Changer[*]")
        self.setWindowModified(self.dirty)

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

    def editUnMirror(self, on):
        if self.image.isNull():
            return
        if self.mirroredhorizontally:
            self.editMirrorHorizontal(False)
        if self.mirroredvertically:
            self.editMirrorVertical(False)

    def editMirrorHorizontal(self, on):
        if self.image.isNull():
            return
        self.image = self.image.mirrored(True, False)
        self.showImage()
        self.mirroredhorizontally = not self.mirroredhorizontally
        self.dirty = True
        self.updateStatus(("Mirrored Horizontally"
                           if on else "Unmirrored Horizontally"))

    def editMirrorVertical(self, on):
        if self.image.isNull():
            return
        self.image = self.image.mirrored(False, True)
        self.showImage()
        self.mirroredvertically = not self.mirroredvertically
        self.dirty = True
        self.updateStatus(("Mirrored Vertically"
                           if on else "Unmirrored Vertically"))

    def showImage(self, percent=None):
        if self.image.isNull():
            return
        self.imageLabel.setPixmap(QPixmap.fromImage(self.image))


app = QApplication(sys.argv)
form = myMainWindow()
form.setMinimumSize(1000, 1000)
form.show()
app.exec_()
