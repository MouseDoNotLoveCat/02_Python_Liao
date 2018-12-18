# -*- coding: utf-8 -*-
# @File  : 10.4_ltertools.py
# @Author: Luhow
# @Date  : 2018/12/13
# @Desc  : litertools


# 求Pi
import itertools
def pi(N):
    odd_liter = itertools.count(1,2)
    ol = itertools.takewhile(lambda x:x <= 2*N-1, odd_liter)
    # x = 0
    # for n in ol:
    #     x = x + (-1)**((n+1)/2+1)*4/n
    # return x
    # 用列表生成器
    list = [(-1)**((n+1)/2+1)*4/n for n in ol]
    return sum(list)


# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')


