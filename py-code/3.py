#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/10/22 10:37
# @Author : Chen Shan
# Function : Solve the problem of chicken and rabbit in the same cage

a = int(input("请输入一个整数（头的个数）:"))
b = int(input("请输入一个整数（腿的个数）:"))
hand = 0
foot = 0
for i in range(0,a+1):
    if i * 2 + (a-i) * 4 == b:
        print("鸡的个数是："+str(i)+"，兔的个数是"+str(a-i))
        break
else:
    print("此输入无解")