#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 如果我们要编写一个搜索引擎，第一步是用爬虫把目标网站的页面抓下来，
# 第二步就是解析该HTML页面，看看里面的内容到底是新闻、图片还是视频。

# 假设第一步已经完成了，第二步应该如何解析HTML呢？

# HTML本质上是XML的子集，但是HTML的语法没有XML那么严格，
# 所以不能用标准的DOM或SAX来解析HTML。

# 好在Python提供了HTMLParser来非常方便地解析HTML，只需简单几行代码：

from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):
    def handle_starttag(self,tag,attrs):
        print('<%s>' % tag)
    def handle_endtag(self,tag):
        print('</%s>' % tag)
    def handle_startendtag(self,tag,attrs):
        print('<%s/>' % tag)
    def handle_data(self,data):
        print(data)
    def handle_comment(self,data):
        print('<!--',data,'-->')
    def handle_entityref(self,name):
        print('&%s;' % name)
    def handle_charref(self,name):
        print('&#%s;' % name)

parser=MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>
''')

# feed()方法可以多次调用，也就是不一定一次把整个HTML字符串都塞进去，
# 可以一部分一部分塞进去。

# 特殊字符有两种，一种是英文表示的&nbsp;，一种是数字表示的&#1234;，
# 这两种字符都可以通过Parser解析出来。



# 小结
# 利用HTMLParser，可以把网页中的文本、图像等解析出来。



# 练习
# 找一个网页，例如https://www.python.org/events/python-events/，
# 用浏览器查看源码并复制，然后尝试解析一下HTML，
# 输出Python官网发布的会议时间、名称和地点。

from urllib import request
from html.parser import HTMLParser
import re 

class MyHTMLParser(HTMLParser):
    flag=0
    res=[]
    is_get_data=0

    def handle_starttag(self, tag, attrs):
        # 首先找到包裹事件的元素
        if tag == 'ul':
            for attr in attrs:
                if re.match(r'list-recent-events', attr[1]):
                    self.flag = 1
        
        # 处理包裹事件名称的a元素
        if tag=='a' and self.flag==1:
            self.is_get_data='title'
        
        # 处理时间的time元素
        if tag=='time' and self.flag==1:
            self.is_get_data='time'
        
        # 处理包裹地点的time元素
        if tag=='span' and self.flag==1:
            self.is_get_data='addr'
        
    def handle_endtag(self,tag):
        if self.flag==1 and tag=='ul':
            self.flag=0
    
    def handle_data(self,data):
        if self.is_get_data and self.flag==1:
            if self.is_get_data=='title':
                self.res.append({self.is_get_data:data})
            else:
                self.res[len(self.res)-1][self.is_get_data]=data
            self.is_get_data=None

parser=MyHTMLParser()

with request.urlopen('https://www.python.org/events/python-events/') as f:
    data=f.read().decode('utf-8')

parser.feed(data)
for item in MyHTMLParser.res:
    print('--------------')
    for k,v in item.items():
        print("%s : %s" % (k,v))
