# _*_ coding: utf-8 _*_
"""@author: Luhow
@time:2018/11/2620:13
"""


def product(*ys):
    if not ys:  # ys如果为空，就是一个空的tuple,=0
        raise TypeError("参数不能为空")
    z = 1
    for y in ys:
        z = z*y
    return z


print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')



