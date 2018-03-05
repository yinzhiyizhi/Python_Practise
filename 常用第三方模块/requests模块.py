#!/usr/bin/env python
# -*- coding: utf-8 -*

# 我们已经讲解了Python内置的urllib模块，用于访问网络资源。
# 但是，它用起来比较麻烦，而且，缺少很多实用的高级功能。

# 更好的方案是使用requests。它是一个Python第三方库，处理URL资源特别方便。



# 安装requests
# 如果安装了Anaconda，requests就已经可用了。
# 否则，需要在命令行下通过pip安装：

# $ pip install requests

# 如果遇到Permission denied安装失败，请加上sudo重试。



# 使用requests
# 要通过GET访问一个页面，只需要几行代码：

import requests
r=requests.get('https://www.douban.com') # 豆瓣首页
r.status_code
# 200
r.text
# r.text
# '<!DOCTYPE HTML>\n<html>\n<head>\n<meta name="description" content="提供图书、电影、音乐唱片的推荐、评论和...'
