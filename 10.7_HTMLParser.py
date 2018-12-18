# -*- coding: utf-8 -*-
# @File  : 10.7_HTMLParser.py
# @Author: Luhow
# @Date  : 2018/12/16
# @Desc  : HTML 解析器

from html.parser import HTMLParser
from html.entities import  name2codepoint
from urllib import request
import re

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super(MyHTMLParser, self).__init__()
        #存储当前标签类型
        self.CurrentData = ""
        #存储上一个标签
        self.previousTag = ""
        #存储所有event
        self.allInfo = list()
        #存储一个会议
        self.event = dict()
    def handle_starttag(self, tag, attrs):
        diyTag = False
        if tag == 'h3' and ('class','event-title') in attrs:
            diyTag = True
            self.previousTag = 'event-title'
        elif tag == 'a' and self.previousTag == 'event-title':
            self.CurrentData = 'event-title'
        elif tag == 'time' and 'datetime':
            self.CurrentData = 'event-time'
        elif tag == 'span' and ('class','event-location') in attrs:
            self.CurrentData = 'event-location'
        elif tag == 'span' and ('class','say-no-more') in attrs and self.previousTag == 'time':
            self.CurrentData = 'event-year'
        else:
            self.CurrentData = ""
            self.previousTag = ""
        if not diyTag:
            self.previousTag = tag

    def handle_endtag(self, tag):
        self.CurrentData = ""

    def handle_startendtag(self, tag, attrs):
        pass

    def handle_data(self, data):
        if self.CurrentData == 'event-title':
            self.event['event-title'] = data
            print('会议主题: %s' % data)
        elif self.CurrentData == 'event-year':
            if re.match(r'[0-9]', data.strip()):
                self.event['event-year'] = data
                print('会议年份: %s' % data)
        elif self.CurrentData == 'event-time':
            self.event['event-time'] = data
            print('会议时间: %s' % data)
        elif self.CurrentData == 'event-location':
            self.event['event-location'] = data
            print('会议地点: %s' % data)
            self.allInfo.append(self.event)
            print('----------------------------------------')


    def handle_comment(self, data):
        #print('<!--', data, '-->')
        pass

    def handle_entityref(self, name):
        #print('&%s;' % name)
        pass

    def handle_charref(self, name):
        #print('&#%s;' % name)
        pass

parser = MyHTMLParser()
URL = 'https://www.python.org/events/python-events/'
with request.urlopen(URL, timeout=4) as f:
    data = f.read()

parser.feed(data.decode('utf-8'))
print(parser.allInfo)