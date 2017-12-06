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


