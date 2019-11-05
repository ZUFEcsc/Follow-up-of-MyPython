#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/5 11:15
# @Author : Chen Shan
# Function :Using Python to crawl useful data in HTML format and store it in dataframe data format

from lxml.html import parse
from urllib.request import urlopen
import pandas as pd

parsed = parse(urlopen('http://info.zufe.edu.cn/xygk/szdw.htm'))
doc = parsed.getroot()
strongs = doc.findall('.//strong')
links = doc.findall('.//a')
tds = doc.findall('.//td')

# for i in strongs:
    # print(i.text_content())
# for j in links:
#     print(j, j.get('href'), j.text_content())
# for item in tds:
#     print(item, item.text_content())
flag = 0
index = 1
dict = {'FULL_NAME':[], 'POSITION':[], 'HOME_LINK':[]}

for item in tds:
    for j in links:
        if item.text_content() == j.text_content():
            if item.text_content() == '信息管理系':
                flag=1
                break
            if j.get('href') != '../index.htm':
                if index <= 14:
                    position = 'Professor'
                elif index <= 45:
                    position = 'Associate professor'
                else:
                    position = 'Lecturer'
                index+=1
                dict['FULL_NAME'].append(j.text_content())
                dict['HOME_LINK'].append(j.get('href'))
                dict['POSITION'].append(position)
                # print(j.text_content(),j.get('href'))
            break
    if flag == 1:
        break
data_frame = pd.DataFrame(dict)
print(data_frame)