#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/10/22 10:37
# @Author : Chen Shan
# Function ：Judge triangle type

a = int(input("请输入一个整数（三角形的边长a）:"))
b = int(input("请输入一个整数（三角形的边长b）:"))
c = int(input("请输入一个整数（三角形的边长c）:"))
if a+b < c or b+c <a or a+c < b:
    print("这三条边无法构成一个三角形")
elif a == b or b == c or a == c:
    print("这是一个等腰三角形")
else:
    print("这是一个三角形")

