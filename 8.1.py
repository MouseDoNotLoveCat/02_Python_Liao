# -*- coding: utf-8 -*-
# @File  : 8.1.py
# @Author: Luhow
# @Date  : 2018-12-05
# @Desc  :  文件读写


fpath = r'c:\windows\system.ini'

with open(fpath, 'r') as f:
    s = f.read()
    print(s)


