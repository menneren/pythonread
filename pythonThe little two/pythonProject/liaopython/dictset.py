names=['Michael','Bob','Tracy']
scores=[95,75,85]

d={'Michael':95,'Bob':75,'Tracy':85}
print(d['Michael'])

#print(d['sds'])   #Traceback (most recent call last):
                  # KeyError: 'sds'
#判断key是否存在
print('Thonme' in d)
print(d.get('YONL'))      #python环境不显示，返回None
print(d.get('YONL'), -1)  #返回None -1

#删除一个key
print(d.pop('Bob'))
print(d)
#查找速度快，占用大量内存
#哈希算法（Hash）

key = [1, 2, 3]
#d[key] = 'a list'   #key的对象就不能变（字符串、整数），而list可变，不能做key

s=set([1,2,3])
print(s)
#重复元素过滤
s=set([1, 1, 2, 2, 3, 4, 3])
print(s)
#可重复，重复添加，无效
s.add(5)
print(s)
s.add(5)
print(s)

s.remove(5)
print(s)

s1=set([1,2,3])
s2=set([2,3,4])
print(s1&s2)
print(s1|s2)

#str是不变对象，而list是可变对象
a=['c','b','a']
a.sort()
print(a)

#不可变对象
a='abc'
print(a.replace('a','A'))
print(a)

