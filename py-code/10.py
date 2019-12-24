#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/12 11:05
# @Author : Chen Shan
# Function : Read mat 3D data & plot analysis

import scipy.io as sio
import math
import matplotlib.pyplot as plt
raw_K=sio.loadmat('../py-data/10_Subject1K.mat')
raw_V=sio.loadmat('../py-data/10_Subject1V.mat')

k = raw_K['Subject1K']
v = raw_V['Subject1V']

subkk = []
subvv = []
index = 0
flag = 0
minnum = 10
maxnum = 30
for ik in k:
    # print(ik)
    for iik in ik:
        # print(iik)
        if index >= minnum:
            if index <=maxnum:
                subkk.append(iik[3])
        elif index > maxnum:
            flag = 1
            break
        index = index + 1
    if flag == 1:
        break
# print(subkk)
# print(index)
index = 0
for iv in v:
    # print(iv)
    for iiv in iv:
        # print(iiv)
        if index >= minnum:
            if index <= maxnum:
                subvv.append(iiv[3])
        elif index > maxnum:
            flag = 1
            break
        index = index + 1
    if flag == 1:
        break

junk = []
sk1 = []
sk2 = []
index = 0
for ik in k:
    for iik in ik:
        if index >= minnum:
            if index <= maxnum:
                tempk = (iik[0]+iik[1]+iik[2]+iik[3])/4
                temps = math.pow((iik[0]-tempk),2)+math.pow((iik[1]-tempk),2)+math.pow((iik[2]-tempk),2)+math.pow((iik[3]-tempk),2)/4
                temps = math.sqrt(temps)
                junk.append(tempk)
                sk1.append(tempk+temps)
                sk2.append(tempk-temps)
        elif index > maxnum:
            flag = 1
            break
        index = index + 1
    if flag == 1:
        break
# print(junk)

fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax1.plot(subkk,'go--',label =  'Subject1K')
ax1.plot(subvv,'bo--',label = 'Subject1V')
ax1.legend(loc='best')
ax2 = fig.add_subplot(2,1,2)
ax2.plot(junk,'go--',label = 'MEAN')
ax2.plot(sk1,'--',label = 'Mean + Variance')
ax2.plot(sk2,'--',label = 'Mean - Variance')
ax2.legend(loc='best')
plt.show()

# print(k)
# print(v)
