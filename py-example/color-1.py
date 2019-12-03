#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/3 11:38
# @Author : ChenShan
# Function :
import sys
from PyQt5.QtWidgets import QWidget, \
    QPushButton, \
    QToolTip, \
    QMessageBox, \
    QApplication, \
    QDesktopWidget, \
    QMainWindow, \
    QAction, \
    qApp, \
    QVBoxLayout, \
    QHBoxLayout, \
    QTextBrowser, \
    QLineEdit, \
    QLabel, \
    QInputDialog, \
    QColorDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, \
    QIcon


# QMainWindow是QWidget的派生类
class CMainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # ToolTip设置
        QToolTip.setFont(QFont('华文楷体', 10))

        # statusBar设置
        self.statusBar().showMessage('准备就绪')

        # 退出Action设置
        exitAction = QAction(QIcon('1.png'), '&Exit', self)
        exitAction.setShortcut('ctrl+Q')
        exitAction.setStatusTip('退出应用程序')
        exitAction.triggered.connect(qApp.quit)  # qApp就相当于QCoreApplication.instance()

        # menuBar设置
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        # toolBar设置
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        # 确认PushButton设置
        btnOK = QPushButton("确认")
        btnOK.setToolTip("点击此按钮将确认改变！")
        btnOK.setStatusTip("点击此按钮将确认改变！")
        btnOK.clicked.connect(self.funOK)
        btnOK.resize(btnOK.sizeHint())

        # 取消PushButton设置
        btnCancel = QPushButton("取消")
        btnCancel.setToolTip("点击此按钮将放弃改变！")
        btnCancel.setStatusTip("点击此按钮将放弃改变！")
        btnCancel.clicked.connect(self.funCancel)
        btnCancel.resize(btnCancel.sizeHint())

        # 退出PushButton设置
        btnQuit = QPushButton('退出')
        btnQuit.setToolTip("点击此按钮将退出应用程序！")
        btnQuit.setStatusTip("点击此按钮将退出应用程序！")
        btnQuit.clicked.connect(qApp.quit)
        btnQuit.resize(btnQuit.sizeHint())

        # 更改提示PushButton设置
        btnTip = QPushButton('更改提示')
        btnTip.setToolTip("点击此按钮将更改提示符！")
        btnTip.setStatusTip("点击此按钮将更改提示符！")
        btnTip.clicked.connect(self.funTip)
        btnTip.resize(btnTip.sizeHint())

        # 更改背景色PushButton设置
        btnBackgroundColor = QPushButton('更改背景色')
        btnBackgroundColor.setToolTip("点击此按钮将更改背景色！")
        btnBackgroundColor.setStatusTip("点击此按钮将更改背景色！")
        btnBackgroundColor.clicked.connect(self.funBackgroundColor)
        btnBackgroundColor.resize(btnBackgroundColor.sizeHint())

        # PushButton布局
        hBox1 = QHBoxLayout()
        hBox1.addStretch(1)
        hBox1.addWidget(btnBackgroundColor)
        hBox1.addWidget(btnTip)
        hBox1.addWidget(btnOK)
        hBox1.addWidget(btnCancel)
        hBox1.addWidget(btnQuit)

        # QTextBrwoser是只读的多行文本框，既可以显示普通文本，又可以显示HTML
        self.textBrowser = QTextBrowser()
        # 提示标签
        self.labTip = QLabel(">>>")
        # 单行文本框
        self.lineEdit = QLineEdit("请输入表达式，然后按确认键")
        self.lineEdit.selectAll()
        self.lineEdit.returnPressed.connect(self.funOK)
        # 布局
        hBox2 = QHBoxLayout()
        hBox2.addWidget(self.labTip)
        hBox2.addWidget(self.lineEdit)

        # 布局
        vBox = QVBoxLayout()
        vBox.addWidget(self.textBrowser)
        vBox.addLayout(hBox2)
        vBox.addLayout(hBox1)
        widget = QWidget()
        self.setCentralWidget(widget)  # 建立的widget在窗体的中间位置
        widget.setLayout(vBox)

        # 布局完毕后，才可得到焦点
        self.lineEdit.setFocus()

        # Window设置
        self.resize(500, 300)
        self.center()
        self.setFont(QFont('华文楷体', 10))
        self.setWindowTitle('PyQt5应用教程（snmplink编著）')
        self.setWindowIcon(QIcon('10.png'))
        self.show()

    def center(self):
        # 得到主窗体的框架信息
        qr = self.frameGeometry()
        # 得到桌面的中心
        cp = QDesktopWidget().availableGeometry().center()
        # 框架的中心与桌面中心对齐
        qr.moveCenter(cp)
        # 自身窗体的左上角与框架的左上角对齐
        self.move(qr.topLeft())

    def funOK(self):
        try:
            text = self.lineEdit.text()
            self.textBrowser.append("{} = <b>{}</b>".format(text, eval(text)))
        except:
            self.textBrowser.append("输入的表达式<font color=red>“{}”</font>无效!".format(text))

    def funCancel(self):
        self.lineEdit.clear()

    def funTip(self):
        # 返回两个值：输入的文本和点击的按钮
        text, ok = QInputDialog.getText(self, '请输入新的提示符', '提示符：')
        if ok:
            self.labTip.setText(text)

    def funBackgroundColor(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.textBrowser.setStyleSheet("QTextBrowser{background-color:%s}" % col.name())

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def closeEvent(self, QCloseEvent):
        reply = QMessageBox.question(self,
                                     'PyQt5应用教程（snmplink编著）',
                                     "是否要退出应用程序？",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = CMainWindow()
    sys.exit(app.exec_())