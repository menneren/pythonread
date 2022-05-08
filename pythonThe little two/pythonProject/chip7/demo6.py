#集合的相关操作
s={10,20,30,405,60}
'''集合元素的判断操作'''
print(10 in s)
print(100 in s)
print(10 not in s)
print(100 not in s)
'''集合元素的判断操作'''
s.add(80)   #一次添中一个元素
print(s)
s.update({200,400,300})  #集合至少添加一个元素
print(s)
s.update([100,99,8])
s.update((78,64,56))
print(s)
'''集合元素的删除操作'''
s.remove(100)
print(s)
#s.remove(500)   KeyError: 500
s.discard(500)
s.discard(300)
print(s)

s.pop()
s.pop()
#s.pop(400)   不能添加参数TypeError: set.pop() takes no arguments (1 given)
print(s)  #删除一个元素
s.clear()
print(s)


