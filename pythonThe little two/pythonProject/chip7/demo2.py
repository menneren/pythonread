t2='Python','world',98
print(t2)
print(type(t2))

t3=('Python',)   #元组种只有一个元素，要加'，'
print(t3)
print(type(t3))

'''第二种创建方式，使用内置函数tuple()'''
t1=tuple(('python','world',98))
print(t1)
print(type(t1))

'''空元组的创建方式'''
'''空列表的创建方式'''
lst=[]
lst1=list()

d={}
d2=dict()

#空元组
t4=()
t5=tuple()

print('空列表',lst)
print('空字典',d,d2)
print('空元组',t4,t5)



