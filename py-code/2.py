#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/10/22 10:37
# @Author : Chen Shan
# Function : Calculate the number of times the paper is folded in half

paper_width = 0.00008
mountain_width = 8848.13
cnt = 0
while True:
    paper_width *= 2
    cnt += 1
    if paper_width >= mountain_width:
        break

print("需要对折"+str(cnt)+"次才可以")