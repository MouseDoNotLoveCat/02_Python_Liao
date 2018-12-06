# -*- coding: utf-8 -*-
# @File  : 6.2.py
# @Author: Luhow
# @Date  : 2018-12-03
# @Desc  : 实例属性和类的属性


class Student(object):
    count: int = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1


if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')
