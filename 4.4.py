# _*_ coding: utf-8 _*_
"""@author: Luhow
@time:2018/11/2620:46
"""


def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n-1, a, c, b)  # 把上面n-1个盘子借助c柱按法则挪到b柱
        move(1, a, b, c)
        # if n > 1:
        #     move(n - 1, b, a, c)  # 递归！把前面挪到b柱的n-1个盘子再借助a柱（盘子现在在b柱），重新执行一遍汉诺塔移动。
        # else:
        #     move(1, b, a, c)  # 如果只剩一个盘子了，直接把它从b柱挪到c柱，完成！
        move(n - 1, b, a, c)  # 递归！把前面挪到b柱的n-1个盘子再借助a柱（盘子现在在b柱），重新执行一遍汉诺塔移动。不用上面的判断了


move(3, 'A', 'B', 'C')




