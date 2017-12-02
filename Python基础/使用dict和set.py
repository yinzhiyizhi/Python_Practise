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



print("set和dict类似，也是一组key的集合，但不存储value。")
print("由于key不能重复，所以，在set中，没有重复的key。")
print("要创建一个set，需要提供一个list作为输入集合：")
s=set([1,2,3])
s
# {1,2,3}
# 注意，传入的参数[1,2,3]是一个list，而显示的{1,2,3}只是告诉你这个set内部
# 有1，2，3这3个元素，显示的顺序也不表示set是有序的。


print("重复元素在set中自动被过滤：")
s=set([1,1,2,2,3,3])
s
#{1,2,3}


print("add(key)添加新元素，重复添加没有效果")
s.add(4)
s
#{1,2,3,4}
s.add(4)
s
#{1,2,3,4}


print("remove(key)删除元素")
s.remove(4)
s
#{1,2,3}


s1=set([1,2,3])
s2=set([2,3,4])
# 交集
s1&s2
# {2,3}
# 并集
s1|s2
# {1,2,3,4}

pritn("set和dict都不可以放入可变对象")








