#!/usr/bin/env python
# -*- coding: utf-8 -*-

# collections是Python内建的一个集合模块，提供了许多有用的集合类。



# namedtuple
# 我们知道tuple可以表示不变集合，例如，一个点的二维坐标就可以表示成：
p=(1,2)

# 但是，看到(1, 2)，很难看出这个tuple是用来表示一个坐标的。

# 定义一个class又小题大做了，这时，namedtuple就派上了用场：
from collections import namedtuple
Point=namedtuple('Point',['x','y'])
p=Point(1,2)
p.x
# 1
p.y
# 2












