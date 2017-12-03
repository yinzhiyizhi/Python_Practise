# 调用绝对值abs函数
abs(100)
# 100
abs(-20)
# 20
abs(12.34)
# 12.34

print("如果调用函数的时候，传入的参数数量不对或参数类型不对")
print("就会报TypeError错误")

print("而max函数max()可以接受任意多个参数，并返回最大的那个")
max(1,2)
# 2
max(2,3,1,-5)
# 3


print("内置的常用函数还包括数据类型转换函数")
print("比如int()函数可以把其他数据类型转换为整数")
int('123')
# 123
int(12.34)
# 12
float('12.34')
# 12.34
str(1.23)
# '1.23'
str(100)
# '100'
bool(1)
# True
bool('')
# False


print("函数名其实就是指向一个函数对象的引用")
print("完全可以吧函数名赋给一个变量")
print("相当于给这个函数起了一个“别名”")
a=abs # 变量a指向abs函数
a(-1) # 所以也可以通过a调用abs函数
# 1



print("练习")
print("请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串")
n1=255
n2=1000
print(str(hex(n1)))
print(str(hex(n2)))




