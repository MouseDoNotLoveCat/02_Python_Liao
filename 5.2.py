# _*_ coding: utf-8 _*_
"""@author: Luhow
@time:2018/12/120:56
Filter
"""


# #　求素数的例子
# def _odd_iter(): #产生一个所有奇数的序列，隋性。因为２以外的偶数肯定不是素数
#     n = 1
#     while True:
#         n = n + 2
#         yield n
#
#
# def _not_divisible(n):  # 筛选函数：如果不能除尽n返回ture，否则返回false
#     return lambda x: x % n > 0
#
# # 定义一个素数生成器
# def primes():
#     yield 2
#     it = _odd_iter() # 初始序列
#     while True:
#         n = next(it) # 返回序列的第一个数
#         yield n
#         it = filter(_not_divisible(n), it) # 去除第一个数的公倍数，构造新序列，
#
# # 打印1000以内的素数:
# for n in primes():
#     if n < 1000:
#         print(n)
#     else:
#         break

# 练习：列出所有正反序相同的数
# 先定义一个过滤函数
def is_palindrome(i):
    s = str(i)
    # s1 = s[::-1]
    return s == s[::-1]


output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')