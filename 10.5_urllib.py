# -*- coding: utf-8 -*-
# @File  : 10.5_urllib.py
# @Author: Luhow
# @Date  : 2018/12/15
# @Desc  : urllib


# 读取JSON


from urllib import request
import json


def fetch_data(url):
    with request.urlopen(url) as f:
        urldata = f.read().decode('utf-8') # 按utf-8解码
        return json.loads(urldata) # 反序列化为python对象，dict


# 测试
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json'
data = fetch_data(URL)
print(data)
assert data['query']['results']['channel']['location']['city'] == 'Beijing'
print('ok')