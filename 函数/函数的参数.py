def power(x):
    return x*x

power(5)
# 25
power(15)
# 225

def power(x,n):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s

power(5,2)
# 25

power(5,3)
# 125


# 设置n的默认值为2
def power(x,n=2):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s

# 此时，调用power(5)相当于调用power(5,2)
power(5)
# 25

power(5,2)
# 25


def enroll(name,gender,age=6,city='Beijing'):
    print('name',name)
    print('gender',gender)
    print('age',age)
    print('city',city)


enroll('Bob','M',7)
enroll('Adam','M',city='Tianjin')



# 关于函数定义的时候，默认参数有个特别需要注意的地方
# 定义默认参数要牢记一点：默认参数必须指向不变对象！
def add_end(L=None):
    if L is None:
        L=[]
    L.append('END')
    return L


# 为什么要设计str、None这样的不变对象呢？
# 因为不变对象一旦创建，对象内部的数据就不能修改,
# 这样就减少了由于修改数据导致的错误。
# 此外，由于对象不变，多任务环境下同时读取对象不需要加锁，
# 同时读一点问题都没有。
# 我们在编写程序时，如果可以设计一个不变对象，
# 那就尽量设计成不变对象。



# 可变参数

def calc(numbers):
    sum=0
    for n in numbers:
        sum=sum+n*n
    return sum

# 此时调用要先组装一个list或tuple
calc([1,2,3])
# 14
calc((1,3,5,7))
# 84

# 利用可变参数之后
def calc(*numbers):
    sum=0
    for n in numbers:
        sum=sum+n*n
    return sum

calc(1,2,3)
# 14
calc(1,3,5,7)
# 84

# 定义可变参数和定义一个list或tuple参数相比，
# 仅仅在参数前面加了一个*号。
# 在函数内部，参数numbers接收到的是一个tuple，
# 因此，函数代码完全不变。
# 但是，调用该函数时，可以传入任意个参数，包括0个参数
calc(1,2)
# 5
calc()
# 0

# 已有一个list或tuple，要调用一个可变参数
# 可以在list或tuple前加一个*号，
# 把list或tuple的元素变成可变参数传进去
nums=[1,2,3]
calc(nums[0], nums[1], nums[2])
# 简化写法
calc(*nums)
# 14
# *nums表示把nums这个list的所有元素作为可变参数传进去。



# 关键字参数

# 可变参数允许你传入0个或任意个参数，
# 这些可变参数在函数调用时自动组装为一个tuple。
# 而关键字参数允许你传入0个或任意个含参数名的参数，
# 这些关键字参数在函数内部自动组装为一个dict。
# 请看示例：
def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)

person('Michael',30)
# name:Michael age:30 other:{}

person('Bob',35,city='Beijing')
# name:Bob age:35 other:{'city':'Beijing'}
person('Adam',45,gender='M',job='Engineer')
# name:Adam age:45 other:{'gender':'M','job':'Engineer'}


#关键字参数有什么用？它可以扩展函数的功能。
# 比如，在person函数里，我们保证能接收到name和age这两个参数，
# 但是，如果调用者愿意提供更多的参数，我们也能收到。
# 试想你正在做一个用户注册的功能，
# 除了用户名和年龄是必填项外，其他都是可选项，
# 利用关键字参数来定义这个函数就能满足注册的需求。


# 和可变参数类似，也可以先组装出一个dict，
# 然后，把该dict转换为关键字参数传进去：
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])
#简化写法
person('Jack', 24, **extra)
# name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
# **extra表示把extra这个dict的所有key-value
# 用关键字参数传入到函数的**kw参数，
# kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，
# 对kw的改动不会影响到函数外的extra。



# 命名关键字参数

# 对于关键字参数，
# 函数的调用者可以传入任意不受限制的关键字参数。
# 至于到底传入了哪些，就需要在函数内部通过kw检查。

# 仍以person()函数为例，我们希望检查是否有city和job参数：
def person(name,age,**kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:',name,'age:',age,'other:',kw)

# 但是调用者仍可以传入不受限制的关键字参数：
person('Jack',24,city='Beijing',addr='Chaoyang',zipcode=123456)

# 如果要限制关键字参数的名字，就可以用命名关键字参数，
# 例如，只接收city和job作为关键字参数。
# 这种方式定义的函数如下:
def person(name,age,*,city,job):
    print(name,age,city,job)

# 和关键字参数**kw不同，
# 命名关键字参数需要一个特殊分隔符*，
# *后面的参数被视为命名关键字参数。
# 调用方式如下：
person('Jack',24,city='Beijing',job='Engineer')
# Jack 24 Beijing Engineer

# 如果函数定义中已经有了一个可变参数，
# 后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def person(name,age,*args,city,job):
    print(name,age,args,city,job)

# 命名关键字参数必须传入参数名，这和位置参数不同。
# 如果没有传入参数名，调用将报错：
# person('Jack', 24, 'Beijing', 'Engineer')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: person() takes 2 positional arguments but 4 were given
# 由于调用时缺少参数名city和job，
# Python解释器把这4个参数均视为位置参数，
# 但person()函数仅接受2个位置参数

# 命名关键字参数可以有缺省值，从而简化调用：
def person(name,age,*,city='Beijing',job):
    print(name,age,city,job)

# 由于命名关键字参数city具有默认值，调用时，可不传入city参数：
person('Jack',24,job='Engineer')
# Jack 24 Beijing Enginneer

# 使用命名关键字参数时，要特别注意，
# 如果没有可变参数，就必须加一个*作为特殊分隔符。
# 如果缺少*，
# Python解释器将无法识别位置参数和命名关键字参数：
def person(name,age,city,job):
    # 缺少*，city和job被视为位置参数
    pass


# 参数组合

# 在Python中定义函数，
# 可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，
# 这5种参数都可以组合使用。
# 但是请注意，参数定义的顺序必须是：
# 必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

# 比如定义一个函数，包含上述若干种参数：
def f1(a,b,c=0,*args,**kw):
    print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)

def f2(a,b,c=0,*,d,**kw):
    print('a=',a,'b=',b,'c=',c,'d=',d,'kw=',kw)

# 在函数调用的时候，
# Python解释器自动按照参数位置和参数名把对应的参数传进去。

f1(1, 2)
# a = 1 b = 2 c = 0 args = () kw = {}
f1(1, 2, c=3)
# a = 1 b = 2 c = 3 args = () kw = {}
f1(1, 2, 3, 'a', 'b')
# a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
f1(1, 2, 3, 'a', 'b', x=99)
# a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
f2(1, 2, d=99, ext=None)
# a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}

# 最神奇的是通过一个tuple和dict，你也可以调用上述函数：
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)
# a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}
args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)
# a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}

# 所以，对于任意函数，
# 都可以通过类似func(*args, **kw)的形式调用它，
# 无论它的参数是如何定义的。

#  虽然可以组合多达5种参数，但不要同时使用太多的组合，
# 否则函数接口的可理解性很差。



# 小结

# Python的函数具有非常灵活的参数形态，
# 既可以实现简单的调用，又可以传入非常复杂的参数。

# 默认参数一定要用不可变对象，
# 如果是可变对象，程序运行时会有逻辑错误！

# 要注意定义可变参数和关键字参数的语法：

# *args是可变参数，args接收的是一个tuple；

# **kw是关键字参数，kw接收的是一个dict。

# 以及调用函数时如何传入可变参数和关键字参数的语法：

# 可变参数既可以直接传入：func(1, 2, 3)，
# 又可以先组装list或tuple，
# 再通过*args传入：func(*(1, 2, 3))；

# 关键字参数既可以直接传入：func(a=1, b=2)，
# 又可以先组装dict，
# 再通过**kw传入：func(**{'a': 1, 'b': 2})。

# 使用*args和**kw是Python的习惯写法，
# 当然也可以用其他参数名，但最好使用习惯用法。

# 命名的关键字参数是为了限制调用者可以传入的参数名，
# 同时可以提供默认值。

# 定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，
# 否则定义的将是位置参数。



# 练习
# 以下函数允许计算两个数的乘积，
# 请稍加改造，变成可接收一个或多个数并计算乘积：
# def product(x, y):
#    return x * y

# 测试
# print('product(5) =', product(5))
# print('product(5, 6) =', product(5, 6))
# print('product(5, 6, 7) =', product(5, 6, 7))
# print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
# if product(5) != 5:
#     print('测试失败!')
# elif product(5, 6) != 30:
#     print('测试失败!')
# elif product(5, 6, 7) != 210:
#     print('测试失败!')
# elif product(5, 6, 7, 9) != 1890:
#     print('测试失败!')
# else:
#     try:
#         product()
#         print('测试失败!')
#     except TypeError:
#         print('测试成功!')


def product(*x):
    if len(x)==0:
        raise TypeError('请输入数字！')
    for i in x:
        if not isinstance(i,(int,float)):
            raise TypeError(i,'错误的数据类型')
    sum=1
    for i in x:
        sum=sum*i
    return sum


# 测试
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')
