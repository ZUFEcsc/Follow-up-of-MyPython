#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/10/22 10:37
# @Author : ChenShan
import numpy as np
from scipy.optimize import leastsq
import matplotlib.pyplot as plt
import random

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
print("a = "+ str(a) + ", b = "+ str(b) + ", c = "+ str(c))
print("cost:" + str(Para[1]))
print("求解的曲线是:  y=" + str(round(a, 2)) + "x*x+" + str(round(b, 2)) + "x+" + str(c))

plt.figure(figsize=(8, 6))
plt.scatter(X, Y, color="green", label="sample data", linewidth=2)
# 画拟合直线
x = np.linspace(0, 12, 100)  ##在0-15直接画100个连续点
y = a * x * x + b * x + c  ##函数式
plt.plot(x, y, color="red", label="solution line", linewidth=2)
plt.legend()  # 绘制图例
plt.show()
