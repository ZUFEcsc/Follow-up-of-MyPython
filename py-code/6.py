#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/10/22 10:37
# @Author : Chen Shan
# Function : Randomly generate 50 points, fit binary function and present

import numpy as np
from scipy.optimize import leastsq
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import random

# 1 ----------二次函数拟合，point （x，y）随机生成
xx = []
yy = []
def A(params, x):
    a, b, c = params
    return a * x ** 2 + b * x + c

def nosie():
    for i in range(0,10):
        x = random.uniform(1,10)
        y = random.uniform(2,30)
        xx.append(x)
        yy.append(y)

nosie()
X = np.array(xx)
Y = np.array(yy)

# 误差函数，即拟合曲线所求的值与实际值的差
def error(params, x, y):
    return A(params, x) - y

# 对参数求解
def slovePara():
    p0 = [10, 10, 10]
    Para = leastsq(error, p0, args=(X, Y))
    return Para

Para = slovePara()
a, b, c = Para[0]
# print("a = "+ str(a) + ", b = "+ str(b) + ", c = "+ str(c))
# print("cost:" + str(Para[1]))
print("y = " + str(round(a, 2)) + "x*x+" + str(round(b, 2)) + "x+" + str(c))

plt.figure(figsize=(8, 6))
plt.scatter(X, Y, color="green", label="sample data", linewidth=2)

x = np.linspace(0, 12, 100)
y = a * x * x + b * x + c
plt.plot(x, y, color="red", label="solution line", linewidth=2)
plt.legend()
plt.show()

# # 2----------指数函数拟合，point x 随机生成
# def A2(x, a, b, c):
#     return a * np.exp(-b * x) + c
# # nosie
# xdata = np.linspace(0, 4, 50)
# y = A2(xdata, 2.5, 1.3, 0.5)
# ydata = y + 0.11 * np.random.normal(size=len(xdata))
#
# plt.plot(xdata, ydata, 'b-')
#
# popt, pcov = curve_fit(A2, xdata, ydata)
# # popt数组中，三个值分别是待求参数a,b,c
# y2 = [A2(i, popt[0], popt[1], popt[2]) for i in xdata]
# plt.plot(xdata, y2, 'r--')
#
# print("y = "+str(popt[0])+" * np.exp(-"+str(popt[1])+" * x) + "+str(popt[2]))
#
# plt.show()
