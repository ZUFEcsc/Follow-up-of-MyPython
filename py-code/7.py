#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/10/29 10:32
# @Author : Chen Shan
# Function : Simple data analysis, read csv file and save it in DataFrame

import os, glob
from pandas import Series,DataFrame

import pandas as pd

csv_file = "../data/7_exrates.csv"
csv_data = pd.read_csv(csv_file,engine='python')
csv_df = DataFrame(csv_data)

# print(csv_df)
# print('-----')
# print(csv_df['Country'])
# print('-----')
# print(csv_df.shape)
# print(csv_df['Currency units per �1'])

shape = csv_df.shape
usa_cur = 0
china_cur = 0
for i in range (shape[0]):
    if csv_df['Country'][i]=='USA':
        usa_cur = csv_df['Currency units per �1'][i]
    if csv_df['Country'][i]=='China':
        china_cur = csv_df['Currency units per �1'][i]
print("Answer 1.  exchange rate value of USA is "+str(usa_cur)+" & exchange rate value of China is "+ str(china_cur))

sum_cur = 0
max_cur = 0
max_country = 0
min_cur = 10010
min_country = 0

print("Answer 3.  Countries with smaller exchange rates than USA are as follows :")
for i in range (shape[0]):
    if csv_df['Currency units per �1'][i]< usa_cur:
        print(csv_df['Country'][i])
    if csv_df['Currency units per �1'][i] > max_cur:
        max_cur = csv_df['Currency units per �1'][i]
        max_country = csv_df['Country'][i]
    if csv_df['Currency units per �1'][i] < min_cur:
        min_cur = csv_df['Currency units per �1'][i]
        min_country = csv_df['Country'][i]
    sum_cur = sum_cur + csv_df['Currency units per �1'][i]
avg_cur = sum_cur / shape[0]

print("Answer 2.   " + max_country  + "with the largest exchange rate value is " + str(max_cur) )
print(" & " + min_country + " with the lowest exchange rate value is " + str(min_cur))
print(" & the average exchange rate value is " +str(avg_cur))