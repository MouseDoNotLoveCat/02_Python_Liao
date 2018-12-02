# _*_ coding: utf-8 _*_
"""@author: Luhow
匿名函数
@time:2018/12/122:57
"""

def is_odd(n):
    return n % 2 == 1

L = list(filter(lambda n : n % 2 == 1, range(1, 20)))
print(L)