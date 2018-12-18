# -*- coding: utf-8 -*-
# @File  : 9正则表达式.py
# @Author: Luhow
# @Date  : 2018-12-09
# @Desc  : 正则表达式

# 练习1：判断邮件地址
import re


def is_valid_email(addr):
    re_email = re.compile(r'^[0-9a-zA-Z]+[0-9a-zA-Z\.]+\@[0-9a-zA-z]+\.com$')
    if re.match(re_email, addr):
        return True
    else:
        return False


# 测试:
# assert is_valid_email('someone@gmail.com')
# assert is_valid_email('bill.gates@microsoft.com')
# assert not is_valid_email('bob#example.com')
# assert not is_valid_email('mr-bob@example.com')
# print('ok')

# 练习2 取出email中的用户名
# 方法一：利用切分
def name_of_email1(addr):
    # 先判断首字母是否为‘<’
    if addr[0] == '<':
        addr = addr[1:]  # 删除'<'
    return re.split(r'[\>\@]', addr)[0]  # 返回地址切分后的第一个子串，就是用户名

# 方法2利用分组


def name_of_email(addr):
    # 分组表达式里要注意：1：加‘？‘0或1，可有可无！2：加‘*’，任意个，可有可无，3：一定要加数量！
    re_email = re.compile(r'<?([a-zA-Z\s]+)>?\s?(\w*)@(\w+.\w+)')
    m_email = re.match(re_email, addr)
    print(m_email.groups())
    if m_email:
        return m_email.group(1)
    else:
        return None


assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')


