# -*- coding: utf-8 -*-
# @File  : 7.1.py
# @Author: Luhow
# @Date  : 2018-12-04
# @Desc  :错误处理


from functools import reduce


def str2num(s: str):
    if s.find('.') != -1:
        return float(s)
    return int(s)


def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)


def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)


main()

