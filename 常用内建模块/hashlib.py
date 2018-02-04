#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 摘要算法简介
# Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等。

# 什么是摘要算法呢？
# 摘要算法又称哈希算法、散列算法。
# 它通过一个函数，
# 把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）。

# 举个例子，你写了一篇文章，
# 内容是一个字符串'how to use python hashlib - by Michael'，
# 并附上这篇文章的摘要是'2d73d4f15c0db7f5ecb321b6a65e5d6d'。
# 如果有人篡改了你的文章，并发表为'how to use python hashlib - by Bob'，
# 你可以一下子指出Bob篡改了你的文章，
# 因为根据'how to use python hashlib - by Bob'计算出的摘要不同于原始文章的摘要。

# 可见，摘要算法就是通过摘要函数f()对任意长度的数据data计算出固定长度的摘要digest，
# 目的是为了发现原始数据是否被人篡改过。

# 摘要算法之所以能指出数据是否被篡改过，就是因为摘要函数是一个单向函数，
# 计算f(data)很容易，但通过digest反推data却非常困难。
# 而且，对原始数据做一个bit的修改，都会导致计算出的摘要完全不同。

# 我们以常见的摘要算法MD5为例，计算出一个字符串的MD5值：
import hashlib
md5=hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

# 计算结果如下：
# d26a53750bc40b38b65a520292f69306

# 如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的：
import hashlib
md5=hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

# 试试改动一个字母，看看计算的结果是否完全不同。
md5=hashlib.md5()
md5.update('How to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())
# 计算结果如下：


# MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示。

# 另一种常见的摘要算法是SHA1，调用SHA1和调用MD5完全类似：














