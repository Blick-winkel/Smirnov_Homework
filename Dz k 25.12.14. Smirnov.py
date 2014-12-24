# -*- coding=utf-8 -*-
import json, urllib2



class Suggester:
    def __init__(self):
        keyword = ''
        suggestions = []

    @property
    def suggestions(self):
        page = urllib2.urlopen('http://suggest-market.yandex.ru/suggest-market?callback=jQuery18208957727742381394_1419441918626&sk=u4a0d5535cd4d85d80092d312c9442620&v=1&yu=3243437191403764350&fact=1&wiz=TrWth&srv=market&part=' + self.keyword +'&pos=1&_=1419442611006')
        text = page.read()
        text = text.decode('utf-8')
        a = []
        for line in text.split('('):
            line = line.strip(')')
            a.append(line)
        s = json.loads(a[1])
        return s[1]


s = Suggester()
s.keyword = 'И'
for i in s.suggestions:
    print i