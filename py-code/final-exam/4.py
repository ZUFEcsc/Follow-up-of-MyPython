#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/24 10:31
# @Author : Chen Shan
# Function :

import json
from lxml import objectify
import pandas as pd

# 将数据加载到一个列表中
df = {'DATE':[], 'MONTH':[], 'WEEK':[],'WEEKDAY':[],'CLOSE':[]}
min6 = 16724.4891
mind = '2017-06-15'
filename = '4.json'
with open(filename) as f:
    data = json.load(f)

    for dict in data:
        df['DATE'].append(dict['date'])
        df['MONTH'].append(dict['month'])
        df['WEEK'].append(dict['week'])
        df['WEEKDAY'].append(dict['weekday'])
        df['CLOSE'].append(dict['close'])

    data_frame = pd.DataFrame(df)
    print(data_frame)

    for i in data_frame:
        if i[1] == 6:
            if float(i[4]) < min6:
                min6 = i[4]
                mind = i[0]

    print('The minimum closing price in June is '+ str(min6)+' , in day : '+ mind)

