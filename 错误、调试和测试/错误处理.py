#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 在程序运行的过程中，如果发生了错误，可以事先约定返回一个错误代码，
# 这样，就可以知道是否有错，以及出错的原因。
# 在操作系统提供的调用中，返回错误码非常常见。
# 比如打开文件的函数open()，
# 成功时返回文件描述符（就是一个整数），出错时返回-1。

# 用错误码来表示是否出错十分不便，
# 因为函数本身应该返回的正常结果和错误码混在一起，
# 造成调用者必须用大量的代码来判断是否出错：
def foo():
    r=some_function()
    if r==(-1):
        return (-1)
    # do something
    return r

def bar():
    r=foo()
    if r==(-1):
        print('Error')
    else:
        pass

# 一旦出错，还要一级一级上报，直到某个函数可以处理该错误（比如，给用户输出一个错误信息）。

# 所以高级语言通常都内置了一套try...except...finally...的错误处理机制，Python也不例外。


# try
# 让我们用一个例子来看看try的机制：
try:
    print('try...')
    r=10/0
    print('result:',r)
except ZeroDivisionError as e:
    print('except:',e)
finally:
    print('finally...')
print('END')









