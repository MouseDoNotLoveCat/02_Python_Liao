# _*_ coding: utf-8 _*_
"""
@author: Luhow
@time:2018/12/122:09
sort
"""

# 对列表进行文字排序
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0]

def by_score(t):
    return t[1]

L1 = sorted(L, key = lambda t:t[0])
print(L1)

L2 = sorted(L, key = by_score, reverse=True)
print(L2)