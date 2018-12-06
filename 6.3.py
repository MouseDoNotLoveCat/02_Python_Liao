# -*- coding: utf-8 -*-
# @File  : 6.3.py
# @Author: Luhow
# @Date  : 2018-12-03
# @Desc  : 枚举类


from enum import Enum


class Gender(Enum):
    Male = 0
    Female = 1


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')
