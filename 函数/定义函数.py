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


