#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/24 10:31
# @Author : Chen Shan
# Function :

from pandas import Series,DataFrame
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

csv_file = "3.csv"
csv_data = pd.read_csv(csv_file,engine='python')
csv_df = DataFrame(csv_data)

# print(csv_df)
# print(csv_df['Max TemperatureF'])
# print(csv_df['Mean TemperatureF'])
# print(csv_df['Min TemperatureF'])
sk1 = []

for i1 in csv_df['Max TemperatureF']:
    sk1.append(i1)
for i2 in csv_df['Mean TemperatureF']:
    sk1.append(i1)
for i3 in csv_df['Min TemperatureF']:
    sk1.append(i1)

sk = np.array(sk1)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(csv_df['Max TemperatureF'],'go--',label = 'Max TemperatureF')
ax.plot(csv_df['Mean TemperatureF'],'ro--',label = 'Mean TemperatureF')
ax.plot(csv_df['Min TemperatureF'],'bo--',label = 'Min TemperatureF')
ax.legend(loc='best')
plt.show()