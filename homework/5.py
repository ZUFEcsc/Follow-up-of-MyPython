#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/10/15 10:40
# @Author : ChenShan

class staff:
    def __init__(self,id_val,name_val,age_val,salary_val):
        self.id = id_val
        self.name = name_val
        self.age = age_val
        self.salary = salary_val
    def __str__(self):
        print("Name:"+self.name)
        print("Id："+str(self.id))
        print("Age:"+str(self.age))
        print("Salary:"+str(self.salary))
    def Chage_val(self,age_val,salary_val):
        self.age = age_val
        self.salary = salary_val
        print("After change: " + str(self.name) + "'s age is " + str(self.age) + ",salary is " + str(self.salary))

class rangeError(Exception):
    pass

while True:
    id_val = input('Input id of this staff :');
    try:
        id_ral = int(id_val)
        break
    except ValueError:
        print(id_val,'Enter illegal characters except number!')

name_val = input('Input name of this staff:')
while True:
    age_val = input('Input age of this staff:')
    try:
        age_ral = int(age_val)
        if age_ral < 18 or age_ral > 60:
            raise rangeError
        break
    except ValueError:
        print(age_val,'Input is not an integer!')
    except rangeError:
        print(age_ral,'Error in input range!')

while True:
    salary_val = input('Input salary of this staff:')
    try:
        salary_ral = int(salary_val)
        break
    except ValueError:
        print(salary_ral,'Input is not an integer!')

peo = staff(id_val,name_val,age_val,salary_val)
peo.__str__()
peo.Chage_val(35,30000)
peo.__str__()