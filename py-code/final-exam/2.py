#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/24 10:31
# @Author : Chen Shan
# Function :

class rangeError(Exception):
    pass

while True:
    a = int(input("请输入一个整数（a）:"))
    b = int(input("请输入一个整数（b）:"))
    try:
        a = int(a)
        b = int(b)
        if b == 0:
            print('Divisor cannot be 0!')
        else:
            print('the answer is '+str(a/b))
        break
    except ValueError:
        print(a,'Input is not an integer!')


