# -*- coding:utf-8 -*-
"""
@Author:luhow@126.com
"""
from math import sqrt  # 注意导入模块的方法


def quadratic(a, b, c):
    if b**2-4*a*c < 0:
        return '无实根'
    else:
        x1 = (-b + sqrt(b * b - 4 * a * c)) / (2 * a)  # 计算符号前后不要留空，定义函数前后留两行
        x2 = (-b - sqrt(b * b - 4 * a * c)) / (2 * a)
        return x1, x2


print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))
print('quadratic(100, 3, 4) =', quadratic(100, 3, 4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
elif quadratic(100, 3, 4) != '无实根':
    print('测试失败')
else:
    print('测试成功')

