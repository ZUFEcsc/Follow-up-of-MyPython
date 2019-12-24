#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/10 11:29
# @Author : Chen Shan
# Function :GUI programming - ground mouse games

import time
import os
import sys
import PyQt5.QtCore as qc
import PyQt5.QtGui as qg
import PyQt5.QtWidgets as qw

import threading as t
import random

import numpy as np
import matplotlib

matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure  # 注意不是pyplot下的那个figure
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Whac-A-Mole")
        MainWindow.resize(750, 639)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Start = QtWidgets.QPushButton(self.centralwidget)
        self.Start.setGeometry(QtCore.QRect(100, 30, 150, 50))
        self.Start.setObjectName("Start")
        self.Pause = QtWidgets.QPushButton(self.centralwidget)
        self.Pause.setGeometry(QtCore.QRect(300, 30, 150, 50))
        self.Pause.setObjectName("Pause")
        self.Stop = QtWidgets.QPushButton(self.centralwidget)
        self.Stop.setGeometry(QtCore.QRect(500, 30, 150, 50))
        self.Stop.setObjectName("Stop")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 100, 150, 150))
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 100, 150, 150))
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(500, 100, 150, 150))
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(100, 250, 150, 150))
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(300, 250, 150, 150))
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(500, 250, 150, 150))
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(100, 400, 150, 150))
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(300, 400, 150, 150))
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(500, 400, 150, 150))
        self.pushButton_9.setText("")
        self.pushButton_9.setObjectName("pushButton_9")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 570, 300, 50))
        font = QtGui.QFont()
        font.setFamily("HanziPen SC")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Score = QtWidgets.QLabel(self.centralwidget)
        self.Score.setGeometry(QtCore.QRect(500, 570, 150, 50))
        font = QtGui.QFont()
        font.setFamily("HanziPen SC")
        font.setPointSize(36)
        self.Score.setFont(font)
        self.Score.setObjectName("Score")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 750, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Whac-A-Mole"))
        self.Start.setText(_translate("MainWindow", "PLAY"))
        self.Pause.setText(_translate("MainWindow", "STOP"))
        self.Stop.setText(_translate("MainWindow", "END"))
        self.label.setText(_translate("MainWindow", "SCORE ："))
        self.Score.setText(_translate("MainWindow", "0"))


class myMainWindow(qw.QMainWindow, Ui_MainWindow):
    # 重载构造函数
    def __init__(self, parent=None):
        # 重载父类构造函数
        super().__init__(parent)
        # 改变窗口显示的title
        self.setWindowTitle("Whac-A-Mole")

        # 调用Ui_MainWindow中的函数来显示界面
        self.setupUi(self)
        self.retranslateUi(self)

        # 难易程度（可调节）
        # 随机产生地鼠的时间(ms)
        self.t2 = 1000
        # 地鼠显示时间(ms)
        self.t1 = 800
        # 游戏总时间(ms)
        self.t3 = 10000
        self.ppp = 0

        # 初始化
        self.init()

        # 动作组（每个按钮的点击效果）
        self.pushButton.clicked.connect(self.action1)
        self.pushButton_2.clicked.connect(self.action2)
        self.pushButton_3.clicked.connect(self.action3)
        self.pushButton_4.clicked.connect(self.action4)
        self.pushButton_5.clicked.connect(self.action5)
        self.pushButton_6.clicked.connect(self.action6)
        self.pushButton_7.clicked.connect(self.action7)
        self.pushButton_8.clicked.connect(self.action8)
        self.pushButton_9.clicked.connect(self.action9)
        self.Start.clicked.connect(self.startGame)
        self.Stop.clicked.connect(self.stopGame)
        self.Pause.clicked.connect(self.pauseGame)

    def init(self):
        # 参数
        # 暂停状态参数(0为不暂停，1为暂停)
        self.isPaused = 0
        # 地鼠图片
        self.p1 = 'QPushButton{background-image:url("pic/3.png")}'
        self.p3 = 'QPushButton{background-image:url("pic/4.png")}'
        # 背景图片
        self.p2 = 'QPushButton{background-image:url("pic/2.png")}'
        # 初始化背景图
        self.pushButton.setStyleSheet(self.p2)
        self.pushButton_2.setStyleSheet(self.p2)
        self.pushButton_3.setStyleSheet(self.p2)
        self.pushButton_4.setStyleSheet(self.p2)
        self.pushButton_5.setStyleSheet(self.p2)
        self.pushButton_6.setStyleSheet(self.p2)
        self.pushButton_7.setStyleSheet(self.p2)
        self.pushButton_8.setStyleSheet(self.p2)
        self.pushButton_9.setStyleSheet(self.p2)

    def showScore(self):
        self.Score.setText(str(self.score))

    def startGame(self):
        # 初始化
        # 分数
        self.score = 0
        # 记录按钮是否有地鼠，0为无，1为有
        self.haveMouse1 = 0
        self.haveMouse2 = 0
        self.haveMouse3 = 0
        self.haveMouse4 = 0
        self.haveMouse5 = 0
        self.haveMouse6 = 0
        self.haveMouse7 = 0
        self.haveMouse8 = 0
        self.haveMouse9 = 0
        # 设置定时器
        # 控制地鼠出现的时间
        self.timer1 = qc.QTimer(self)
        # 控制随机产生地鼠的时间
        self.timer2 = qc.QTimer(self)
        self.timer2.timeout.connect(self.CreateMouse)
        self.timer2.start(self.t2)
        # 控制游戏总时间
        self.timer3 = qc.QTimer(self)
        self.timer3.timeout.connect(self.gameOver)
        self.timer3.start(self.t3)
        # 初始化分数显示
        self.label.setText("SCORE ：")
        self.Score.setText(str(self.score))

    def pauseGame(self):
        # 如果在没有暂停时按了暂停按钮
        if self.isPaused == 0:
            # 改变暂停状态
            self.isPaused = 1
            # 改变按键显示内容
            self.Pause.setText("CONTINUE")
            # 关闭定时器
            self.timer2.stop()
            # 初始化背景图
            self.pushButton.setStyleSheet(self.p2)
            self.pushButton_2.setStyleSheet(self.p2)
            self.pushButton_3.setStyleSheet(self.p2)
            self.pushButton_4.setStyleSheet(self.p2)
            self.pushButton_5.setStyleSheet(self.p2)
            self.pushButton_6.setStyleSheet(self.p2)
            self.pushButton_7.setStyleSheet(self.p2)
            self.pushButton_8.setStyleSheet(self.p2)
            self.pushButton_9.setStyleSheet(self.p2)

        # 如果在暂停时按了继续按钮
        elif self.isPaused == 1:
            # 改变暂停状态
            self.isPaused = 0
            # 改变按键显示内容
            self.Pause.setText("STOP")
            # 重新打开定时器
            self.timer2.start(self.t2)

    def gameOver(self):
        if self.ppp != 0:
            self.timer3.stop()
            self.label.setText("GAME OVER！FINAL SCORE :")
            self.Score.setText(str(self.score))
            self.timer1.stop()
            self.timer2.stop()
        self.ppp += 1
        # 初始化背景图
        self.pushButton.setStyleSheet(self.p2)
        self.pushButton_2.setStyleSheet(self.p2)
        self.pushButton_3.setStyleSheet(self.p2)
        self.pushButton_4.setStyleSheet(self.p2)
        self.pushButton_5.setStyleSheet(self.p2)
        self.pushButton_6.setStyleSheet(self.p2)
        self.pushButton_7.setStyleSheet(self.p2)
        self.pushButton_8.setStyleSheet(self.p2)
        self.pushButton_9.setStyleSheet(self.p2)

    def stopGame(self):
        self.timer3.stop()
        self.label.setText("GAME OVER！FINAL SCORE :")
        self.Score.setText(str(self.score))
        self.timer1.stop()
        self.timer2.stop()
        # 初始化背景图
        self.pushButton.setStyleSheet(self.p2)
        self.pushButton_2.setStyleSheet(self.p2)
        self.pushButton_3.setStyleSheet(self.p2)
        self.pushButton_4.setStyleSheet(self.p2)
        self.pushButton_5.setStyleSheet(self.p2)
        self.pushButton_6.setStyleSheet(self.p2)
        self.pushButton_7.setStyleSheet(self.p2)
        self.pushButton_8.setStyleSheet(self.p2)
        self.pushButton_9.setStyleSheet(self.p2)

    # 点击地鼠后地鼠消失
    def action1(self):
        # 如果有地鼠
        if self.haveMouse1 == 1:
            self.haveMouse1 = 0
            # 点击后图变成背景图
            self.pushButton.setStyleSheet(self.p2)
            # 分数+1
            self.score += 1
            self.showScore()

    def action2(self):
        # 如果有地鼠
        if self.haveMouse2 == 1:
            self.haveMouse2 = 0
            # 点击后图变成背景图
            self.pushButton_2.setStyleSheet(self.p2)
            # 分数+1
            self.score += 1
            self.showScore()

    def action3(self):
        # 如果有地鼠
        if self.haveMouse3 == 1:
            self.haveMouse3 = 0
            # 点击后图变成背景图
            self.pushButton_3.setStyleSheet(self.p2)
            # 分数+1
            self.score += 1
            self.showScore()

    def action4(self):
        # 如果有地鼠
        if self.haveMouse4 == 1:
            self.haveMouse4 = 0
            # 点击后图变成背景图
            self.pushButton_4.setStyleSheet(self.p2)
            # 分数+1
            self.score += 1
            self.showScore()

    def action5(self):
        # 如果有地鼠
        if self.haveMouse5 == 1:
            self.haveMouse5 = 0
            # 点击后图变成背景图
            self.pushButton_5.setStyleSheet(self.p2)
            # 分数+1
            self.score += 1
            self.showScore()

    def action6(self):
        # 如果有地鼠
        if self.haveMouse6 == 1:
            self.haveMouse6 = 0
            # 点击后图变成背景图
            self.pushButton_6.setStyleSheet(self.p2)
            # 分数+1
            self.score += 1
            self.showScore()

    def action7(self):
        # 如果有地鼠
        if self.haveMouse7 == 1:
            self.haveMouse7 = 0
            # 点击后图变成背景图
            self.pushButton_7.setStyleSheet(self.p2)
            # 分数+1
            self.score += 1
            self.showScore()

    def action8(self):
        # 如果有地鼠
        if self.haveMouse8 == 1:
            self.haveMouse8 = 0
            # 点击后图变成背景图
            self.pushButton_8.setStyleSheet(self.p2)
            # 分数+1
            self.score += 1
            self.showScore()

    def action9(self):
        # 如果有地鼠
        if self.haveMouse9 == 1:
            self.haveMouse9 = 0
            # 点击后图变成背景图
            self.pushButton_9.setStyleSheet(self.p2)
            # 分数+1
            self.score += 1
            self.showScore()

    # 地鼠自动消失
    def stop1(self):
        self.haveMouse1 = 0
        # 显示背景图
        self.pushButton.setStyleSheet(self.p2)

    def stop2(self):
        self.haveMouse2 = 0
        # 显示背景图
        self.pushButton_2.setStyleSheet(self.p2)

    def stop3(self):
        self.haveMouse3 = 0
        # 显示背景图
        self.pushButton_3.setStyleSheet(self.p2)

    def stop4(self):
        self.haveMouse4 = 0
        # 显示背景图
        self.pushButton_4.setStyleSheet(self.p2)

    def stop5(self):
        self.haveMouse5 = 0
        # 显示背景图
        self.pushButton_5.setStyleSheet(self.p2)

    def stop6(self):
        self.haveMouse6 = 0
        # 显示背景图
        self.pushButton_6.setStyleSheet(self.p2)

    def stop7(self):
        self.haveMouse7 = 0
        # 显示背景图
        self.pushButton_7.setStyleSheet(self.p2)

    def stop8(self):
        self.haveMouse8 = 0
        # 显示背景图
        self.pushButton_8.setStyleSheet(self.p2)

    def stop9(self):
        self.haveMouse9 = 0
        # 显示背景图
        self.pushButton_9.setStyleSheet(self.p2)

    # 随机产生地鼠
    def CreateMouse(self):
        # 在数组name中随机一个控件名
        temp = random.randint(1, 9)
        # 将随机到的按钮显示地鼠
        if temp == 1:
            self.pushButton.setStyleSheet(self.p1)
            self.haveMouse1 = 1
            # 打开一次性计时器
            self.timer1.singleShot(self.t1, self.stop1)
        elif temp == 2:
            self.pushButton_2.setStyleSheet(self.p3)
            self.haveMouse2 = 1
            # 打开一次性计时器
            self.timer1.singleShot(self.t1, self.stop2)
        elif temp == 3:
            self.pushButton_3.setStyleSheet(self.p1)
            self.haveMouse3 = 1
            # 打开一次性计时器
            self.timer1.singleShot(self.t1, self.stop3)
        elif temp == 4:
            self.pushButton_4.setStyleSheet(self.p3)
            self.haveMouse4 = 1
            # 打开一次性计时器
            self.timer1.singleShot(self.t1, self.stop4)
        elif temp == 5:
            self.pushButton_5.setStyleSheet(self.p1)
            self.haveMouse5 = 1
            # 打开一次性计时器
            self.timer1.singleShot(self.t1, self.stop5)
        elif temp == 6:
            self.pushButton_6.setStyleSheet(self.p1)
            self.haveMouse6 = 1
            # 打开一次性计时器
            self.timer1.singleShot(self.t1, self.stop6)
        elif temp == 7:
            self.pushButton_7.setStyleSheet(self.p1)
            self.haveMouse7 = 1
            # 打开一次性计时器
            self.timer1.singleShot(self.t1, self.stop7)
        elif temp == 8:
            self.pushButton_8.setStyleSheet(self.p3)
            self.haveMouse8 = 1
            # 打开一次性计时器
            self.timer1.singleShot(self.t1, self.stop8)
        elif temp == 9:
            self.pushButton_9.setStyleSheet(self.p1)
            self.haveMouse9 = 1
            # 打开一次性计时器
            self.timer1.singleShot(self.t1, self.stop9)


app = qw.QApplication(sys.argv)
form = myMainWindow()
# 设定最小的程序窗口大小
form.setMinimumSize(750, 700)
form.show()
app.exec_()

