#S = πr2

r1 = 12.34
r2 = 9.08
r3 = 73.1
s1 = 3.14 * r1 * r1
s2 = 3.14 * r2 * r2
s3 = 3.14 * r3 * r3

#绝对值函数abs
print(abs(100))
print(abs(-10))
print(abs(12.34))

#abs有且仅有一个参数
#print(abs(1,2))

#参数类型不对报错str
#print(abs('a'))    #type

#可以接受任意多个参数，返回最大的那个
print(max(1,2))
print(max(2,3,1,-5))

#数据类型转换
print(int('123'))  #123
print(int(12.34))  #12
print(float('12.34'))  #12.34
print(str(1.23))  #'1.23'
print(str(100))  #'100'
print(bool(1))  #True
print(bool(''))  #False

a = abs # 变量a指向abs函数
print(a(-1)) # 所以也可以通过a调用abs函数

# -*- coding: utf-8 -*-

n1 = 255
n2 = 1000
a=hex(n1)
b=hex(n2)
print(a)
print(b)

x = abs(100)
y = abs(-20)
print(x, y)
print('max(1, 2, 3) =', max(1, 2, 3))
print('min(1, 2, 3) =', min(1, 2, 3))
print('sum([1, 2, 3]) =', sum([1, 2, 3]))