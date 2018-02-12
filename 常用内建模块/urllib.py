#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

# 如果我们要想模拟浏览器发送GET请求，就需要使用Request对象，通过往Request对象添加HTTP头，我们就可以把请求伪装成浏览器。例如，模拟iPhone 6去请求豆瓣首页：














