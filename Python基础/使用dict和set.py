# -*- coding: utf-8 -*-

print("例子1")
d={'A':11,'B':12,'C':13}
print(d['A'])


print("例子2")
d['AAA']=12
print(d['AAA'])


print("例子3")
d['BBB']=13
print(d['BBB'])

d['BBB']=14
print(d['BBB'])


print("通过in判定key是否存在")
print('CCC' in d)


print("通过get（）方法判定key，不存在，则返回None，或者自己指定的value")
print(d.get('CCC'))
print(d.get('CCC',-1))


print("删除一个key，用pop（key）方法")
print(d.pop('B'))
d




