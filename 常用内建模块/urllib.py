#!/usr/bin/env python
# -*- coding: utf-8 -*-

# urllib提供了一系列用于操作URL的功能。



# Get
# urllib的request模块可以非常方便地抓取URL内容，
# 也就是发送一个GET请求到指定的页面，然后返回HTTP的响应：

# 例如，对豆瓣的一个URLhttps://api.douban.com/v2/book/2129650进行抓取，
# 并返回响应：

from urllib import request

with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data=f.read()
    print('Status:',f.status,f.reason)
    for k,v in f.getheaders():
        print('%s: %s' % (k,v))
    print('Data:',data.decode('utf-8'))

# 可以看到HTTP响应的头和JSON数据：

# Status: 200 OK
# Server: nginx
# Date: Tue, 26 May 2015 10:02:27 GMT
# Content-Type: application/json; charset=utf-8
# Content-Length: 2049
# Connection: close
# Expires: Sun, 1 Jan 2006 01:00:00 GMT
# Pragma: no-cache
# Cache-Control: must-revalidate, no-cache, private
# X-DAE-Node: pidl1
# Data: {"rating":{"max":10,"numRaters":16,"average":"7.4","min":0},"subtitle":"","author":["廖雪峰编著"],"pubdate":"2007-6",...}

# 如果我们要想模拟浏览器发送GET请求，就需要使用Request对象，
# 通过往Request对象添加HTTP头，我们就可以把请求伪装成浏览器。
# 例如，模拟iPhone 6去请求豆瓣首页：

from urllib import request

req=request.Request('http://www.douban.com/')
req.add_header('User-Agent','Mozilla/6.0(iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print('Status:',f.status,f.reason)
    for k,v in f.getheaders():
        print('%s: %s' % (k,v))
    print('Data:',f.read().decode('utf-8'))

# 这样豆瓣会返回适合iPhone的移动版网页：

# ...
#     <meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0">
#     <meta name="format-detection" content="telephone=no">
#     <link rel="apple-touch-icon" sizes="57x57" href="http://img4.douban.com/pics/cardkit/launcher/57.png" />
# ...



# Get
# urllib的request模块可以非常方便地抓取URL内容，
# 也就是发送一个GET请求到指定的页面，然后返回HTTP的响应：

# 例如，对豆瓣的一个URLhttps://api.douban.com/v2/book/2129650进行抓取，
# 并返回响应：

from urllib import request

with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data=f.read()
    print('Status:',f.status,f.reason)
    for k,v in f.getheaders():
        print('%s: %s' % (k,v))
    print('Data:',data.decode('utf-8'))

# 可以看到HTTP响应的头和JSON数据：

# Status: 200 OK
# Server: nginx
# Date: Tue, 26 May 2015 10:02:27 GMT
# Content-Type: application/json; charset=utf-8
# Content-Length: 2049
# Connection: close
# Expires: Sun, 1 Jan 2006 01:00:00 GMT
# Pragma: no-cache
# Cache-Control: must-revalidate, no-cache, private
# X-DAE-Node: pidl1
# Data: {"rating":{"max":10,"numRaters":16,"average":"7.4","min":0},"subtitle":"","author":["廖雪峰编著"],"pubdate":"2007-6",...}

# 如果我们要想模拟浏览器发送GET请求，就需要使用Request对象，
# 通过往Request对象添加HTTP头，我们就可以把请求伪装成浏览器。
# 例如，模拟iPhone 6去请求豆瓣首页：

from urllib import request

req=request.Request('http://www.douban.com')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print('Status:',f.status,f.reason)
    for k,v in f.getheaders():
        print('%s: %s' % (k,v))
    print('Data:',f.read().decode('utf-8'))

# 这样豆瓣会返回适合iPhone的移动版网页：

# ...
#     <meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0">
#     <meta name="format-detection" content="telephone=no">
#     <link rel="apple-touch-icon" sizes="57x57" href="http://img4.douban.com/pics/cardkit/launcher/57.png" />
# ...









