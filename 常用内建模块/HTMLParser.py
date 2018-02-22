#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 如果我们要编写一个搜索引擎，第一步是用爬虫把目标网站的页面抓下来，
# 第二步就是解析该HTML页面，看看里面的内容到底是新闻、图片还是视频。

# 假设第一步已经完成了，第二步应该如何解析HTML呢？

# HTML本质上是XML的子集，但是HTML的语法没有XML那么严格，
# 所以不能用标准的DOM或SAX来解析HTML。

# 好在Python提供了HTMLParser来非常方便地解析HTML，只需简单几行代码：













