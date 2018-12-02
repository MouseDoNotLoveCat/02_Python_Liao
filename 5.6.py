# _*_ coding: utf-8 _*_
"""@author: Luhow
@time:2018/12/123:05
装饰器
"""

import time, functools

def metric(fn):
    def int_time(*args):
        start_time = time.perf_counter()
        fn(*args) #可变参数
        over_time = time.perf_counter()
        total_time =(over_time-start_time)
        print('%s executed in %s second' % (fn.__name__,total_time))
        return fn(*args)
    return int_time

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')