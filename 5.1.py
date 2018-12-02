from functools import reduce


# _*_ coding: utf-8 _*_
"""@author: Luhow
函数式编程，高级函数 map and reduce
@time:2018/12/19:35
"""

#  练习


def normalize(name):
    return name.capitalize()
# 测试：


# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)

# def prod(L):
#     def pro(x1, x2):
#         return x1*x2
#     return reduce(pro, L)
#
#
# print(prod([1, 2, 3, 4]))
#
# # 测试
# print('3*5*7*9 = ', prod([3, 5, 7, 9]))
# if prod([3, 5, 7, 9]) == 945:
#     print('测试成功')
# else:
#     print('测试失败')


# 字符串转浮点数，自己的方法是先把数字分为整数和小数两部分，不够简洁
# def str2float(s):
#     # 先定义一个对应字典：
#     DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#
#     # 先区分整数和小数部分，返回整数和小数部分两个字符串，及小数位数，如果没有小数，小数位数返回0
#     def checkpoint(x):
#         pointpos = x.find('.')
#         if pointpos > 0:
#             x1 = x[0:pointpos]
#             x2 = x[pointpos+1:]
#             x3 = len(x) - pointpos-1
#         elif pointpos == 0:
#             x1 = ['0']
#             x2 = x[pointpos + 1:]
#             x3 = len(x) - pointpos - 1
#         else:
#             x1 = x
#             x2 = ['0']
#             x3 = 0
#         return x1, x2, x3
#
#     def char2num(s1):  # 根据传入字符转换成数字
#         return DIGITS[s1]
#
#     def str2int(x, y):  # 给整加上位数信息
#         return x*10+y
#
#     str1, str2, pn = checkpoint(s)
#     if pn > 0:
#         return reduce(str2int, map(char2num, str1)) + reduce(str2int, map(char2num, str2))/(10**pn)
#     else:  # 没有小数
#         return reduce(str2int, map(char2num, str1))

# 老师的方法,以-1表示小数点。
def str2float(s):
    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.': -1}

    def char2num(s1):  # 根据传入字符转换成数字
        return DIGITS[s1]
    point = 0
    def str2int(x, y):  # 给整加上位数信息,一位一位来，如果遇到小数点，设point=1，返回原值，后面改乘为除。
        nonlocal point
        if x == -1: # 第一位就是小数点
            point = 10
            return y/point
        elif y == -1 : # 小数点
            point = 1
            return x
        elif point == 0: # 整数部分
            return x * 10 + y
        else:  # 小数部分
            point = point*10
            return x+y/point
    return reduce(str2int, map(char2num,s))




print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')







