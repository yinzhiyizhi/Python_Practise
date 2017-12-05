# 自定义一个求绝对值的my_abs函数
def my_abs(x):
    if x>=0:
        return x
    else:
        return -x

print(my_abs(-99))
# 99


# 定义一个空函数
def nop():
    pass # pass可以用来作为占位符

# pass还可以这样
age=18
if age>=18:
    pass


# 修改my_abs定义，对参数类型做检查，只允许整数和浮点数类型的参数
# 数据类型检查可以用内置函数isinstance()实现
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x>=0:
        return x
    else:
        return -x


# 返回多个值
# import math 语句表示导入math包
# 并允许后续代码引用math包里的sin、cos函数
import math 

def move(x,y,step,angle=0):
    nx=x+step*math.cos(angle)
    ny=y-step*math.sin(angle)
    return nx,ny

x,y=move(100,100,60,math.pi/6)
print(x,y)

r=move(100,100,60,math.pi/6)
print(r)

# Python的函数返回值是一个tuple




# 定义一个函数quadratic(a,b,c)，接受3个参数
# 返回一元二次方程：ax^2+bx+c=0的两个解
# 计算平方根可以调用math.sqrt()函数
import math
def quadratic(a,b,c):
    for i in (a,b,c):
        if not isinstance(i,(int,float)):
            raise TypeError('输入的参数类型错误')
        elif a==0:
            raise TypeError('a不能等于零')
        else:
            x1=-b+(math.sqrt(b*b-4*a*c))/2*a
            x2=-b-(math.sqrt(b*b-4*a*c))/2*a

A=int(input('please enter your a'))
B=int(input('please enter your b'))
C=int(input('please enter your c'))
print(quadratic(A,B,C))