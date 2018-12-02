# -*- coding:utf-8 -*-
"""
@Author:luhow@126.com
高级特性：迭代器
"""


def triangles1():  # 传统方法，没有直接利用列表生成器简洁
    b1 = []
    while True:
        # n = 1
        b2 = []
        a = 0
        for x in b1:
            b2.append(a+x)
            a = x
        b2.append(1)
        b1 = b2
        # print(b2)
        yield b2


def triangles():  # 利用列表生成器，牛逼！
    L = [1]
    while True:
        yield L
        L = ([1]+[L[i]+L[i+1] for i in range(len(L)-1)]+[1])


d = triangles()
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')