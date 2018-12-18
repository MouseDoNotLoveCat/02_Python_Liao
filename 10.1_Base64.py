# -*- coding: utf-8 -*-
# @File  : 10.1_Base64.py
# @Author: Luhow
# @Date  : 2018-12-09
# @Desc  : Base64


import base64


def safe_base64_decode1(s):
    n = len(s) % 4
    if n > 0:
        i = 0
        while i < n:
            s += b'='
            i += 1
    s = s + b'=' * n
    print(s)
    return base64.urlsafe_b64decode(s)


# print(safe_base64_decode('YWJjZA=='))


def safe_base64_decode(s):
    if not isinstance(s, bytes):  # 判断是否为bytes(以字节为单位）
        s = s.encode('ascii')  # 转换为bytes类型
    s += b'='*(len(s) % 4)  # 只有bytes才能进行这种运算
    return base64.urlsafe_b64decode(s)


# 测试:
assert b'abcd' == safe_base64_decode(b'YWJjZA==')
assert b'abcd' == safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA')
assert b'abcd' == safe_base64_decode('YWJjZA')
print('ok')

