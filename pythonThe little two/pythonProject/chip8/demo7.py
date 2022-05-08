s='hello,python'
print('1.',s.isidentifier())   #False
print('2.','hello'.isidentifier())  #True
print('3.','张三_'.isidentifier())
print('4.','张三_123'.isidentifier())

print('5.','\t'.isspace())   #True

print('6.','abc'.isalpha())   #True
print('7.','张三'.isalpha())
print('8.',' 张三'.isalpha())




