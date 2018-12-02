# -*- coding:utf-8 -*-
"""
@Author:luhow@126.com
主题：切片
"""


# def trim(s): #利用for循环遍历
#     n = 0
#     for a in s:
#         if a == ' ':
#             n += 1
#         else:
#             break
#     s = s[n:]
#     n = 0
#     for a in reversed(s):
#         if a == ' ':
#             n += 1
#         else:
#             break
#     s = s[:len(s)-n]
#     return s
def trim(s):  # 利用while一个一个排除，更加巧妙
    while s[0:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-1]
    return s


print(trim('   check   '))

# if trim('hello ')!='hello':
#     print('测试失败')
# elif trim(' hello')!='hello':
#     print('测试失败')
# elif trim(' hello ')!='hello':
#     print('测试失败')
# elif trim(' hello world ')!='hello world':
#     print('测试失败')
# elif trim('')!='':
#     print('测试失败')
# elif trim(' ')!='':
#     print('测试失败')
# else:
#     print('测试成功')

