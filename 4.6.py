# -*- coding:utf-8 -*-
"""
@Author:luhow@126.com
迭代
"""


def findMinAndMax(L):
    if L:
        max = L[0]
        min = L[0]
        for a in L:
            if max < a:
                max = a
            elif min > a:
                min = a
        return (min, max)
    else:
        return (None, None)


print(findMinAndMax([12,443,32]))
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
