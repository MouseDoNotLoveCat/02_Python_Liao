# -*- coding: utf-8 -*-
# @File  : 10.6_xml.py
# @Author: Luhow
# @Date  : 2018/12/15
# @Desc  : xml 解析xml代码


from xml.parsers.expat import ParserCreate
from urllib import request

class MySaxHandler(object):
    def __init__(self):
        self.forecast = list()

    def start_element(self, name, attrs):
        if name == 'yweather:location':
            self.city = attrs['city']
            print('城市名称：%s' % self.city)
        elif name == 'yweather:forecast':
            self.forecast.append({'date': attrs['date'], 'high': attrs['high'], 'low': attrs['low']})
            # self.forecast
    def end_element(self, name):
        pass

    def char_data(self, text):
        pass

        # if attr.get("city"):
        #     self.result['city'] = attr ["city"]
        # if attr.get("date") and not attr.get("temp"):
        #     self.result["forecast"].appen(dict(date = attr["date"],high = attr["high"], low = attr["low"]))

def parseXml(xml_str):
    print(xml_str)
    parser = ParserCreate()
    handler = MySaxHandler()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml_str)
    return  {
        'city': handler.city,
        'forecast': handler.forecast
    }

# 测试:
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'

with request.urlopen(URL, timeout=4) as f:
    data = f.read()

result = parseXml(data.decode('utf-8'))
print(result)
assert result['city'] == 'Beijing'