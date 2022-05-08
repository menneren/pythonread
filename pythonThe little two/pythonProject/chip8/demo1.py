#字符串的查询操作
s='hello,hello'
print(s.index('lo'))
print(s.find('lo'))
print(s.rindex('lo'))
print(s.rfind('lo'))

print(s.find('k'))   #-1,没有
#print(s.rindex('k'))
print(s.rfind('k'))  #-1


