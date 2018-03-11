#!/usr/bin/env python
# -*- coding: utf-8 -*

# 用Python来编写脚本简化日常的运维工作是Python的一个重要用途。
# 在Linux下，有许多系统命令可以让我们时刻监控系统运行的状态，
# 如ps，top，free等等。
# 要获取这些系统信息，Python可以通过subprocess模块调用并获取结果。
# 但这样做显得很麻烦，尤其是要写很多解析代码。

# 在Python中获取系统信息的另一个好办法是使用psutil这个第三方模块。
# 顾名思义，psutil = process and system utilities，
# 它不仅可以通过一两行代码实现系统监控，还可以跨平台使用，
# 支持Linux／UNIX／OSX／Windows等，
# 是系统管理员和运维小伙伴不可或缺的必备模块。



# 安装psutil
# 如果安装了Anaconda，psutil就已经可用了。
# 否则，需要在命令行下通过pip安装：

# $ pip install psutil

# 如果遇到Permission denied安装失败，请加上sudo重试。



# 获取CPU信息
# 我们先来获取CPU的信息：
import psutil
psutil.cpu_count() # CPU逻辑数量
# 4
psutil.cpu_count(logical=False) # CPU物理核心
# 2
# 2说明是双核超线程，4则是4核非超线程

# 统计CPU的用户／系统／空闲时间：

psutil.cpu_times()
# scputimes(user=10963.31, nice=0.0, system=5138.67, idle=356102.45)

# 再实现类似top命令的CPU使用率，每秒刷新一次，累计10次：

for x in range(10):
    psutil.cpu_percent(interval=1,percpu=True)

# [21.5, 20.0, 15.4, 24.6]
# [29.2, 17.2, 21.9, 35.9]
# [26.6, 18.8, 20.3, 25.0]
# [29.2, 25.0, 32.8, 31.2]
# [21.9, 23.4, 21.5, 27.7]
# [36.4, 32.8, 29.7, 31.2]
# [28.8, 9.4, 15.6, 12.5]
# [23.4, 19.0, 21.9, 24.6]
# [16.9, 9.4, 15.6, 14.1]
# [33.3, 21.9, 28.1, 30.8]


