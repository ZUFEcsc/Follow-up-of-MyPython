#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/5 10:53
# @Author : Chen Shan
# Function :Using Python to read data in XML format and store it in data frame format

from lxml import objectify
import xml.etree.cElementTree as et   # 读取xml文件的包
import pandas as pd

xml_tree = et.ElementTree(file='../py-data/8_cd_catalog.xml')  # 文件路径
dict = {'TITLE':[], 'ARTIST':[], 'COUNTRY':[],'COMPANY':[],'PRICE':[],'YEAR':[]}

root = xml_tree.getroot()

for sub_node in root:
    for node in sub_node:
        # print(node, node.tag, node.attrib, node.text)
        dict[node.tag].append(node.text)
data_frame = pd.DataFrame(dict)
print(data_frame)