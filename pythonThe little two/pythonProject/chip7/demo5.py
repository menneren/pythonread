s=[2,3,4,5,5,6,7,7,8]
print(s)

'''第二中创建方式使用set()'''
sl=set(range(6))
print(sl,type(sl))

s2=set([1,2,3,4,5,5,5,6,6])
print(s2,type(s2))

s3=set((1,2,3,4,5,5,5,65))  #集合中的元素是无序的
print(s3,type(s3))

s4=set('python')
print(s4,type(s4))

s5=set({12,4,34,55,66,44,4})
print(s5,type(s5))

#定义一个空集合
s6={}
print(s6,type(s6))

