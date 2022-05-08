lst=[10,20,30,40,50,60,30]
lst.remove(30)
print(lst)

#pop()根据索引移除元素
lst.pop(1)
print(lst)
#lst.pop(5)   #IndexError: pop index out of range没有就抛出异常

print('------切片操作-删除至少一个元素，将产生一个新的列表对象----------')
new_list=lst[1:3]
print('愿列表',lst)
print('切片后的列表',new_list)

'''不产生新的列表对象，而是删除原列表中的内容'''
lst[1:3]=[]
print(lst)

lst.clear()
print(lst)

del lst
print(lst)
