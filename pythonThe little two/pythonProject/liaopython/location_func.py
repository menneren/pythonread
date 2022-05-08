def power(x):
    return x*x
print(power(5))

#计算x^n
def power(x,n):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s

print(power(5,4))

#默认参数，旧代码失效
#power(5)

def power(x,n=2):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s

print(power(5))
print(power(5,3))

def enroll(name,gender):
    print('name:',name)
    print('gender:',gender)
a=enroll('Sarah','F')
print(a)

def enroll(name,gender,age=6,city='Beijing'):
    print('name:',name)
    print('gender:',gender)
    print('age:',age)
    print('city:',city)
a=enroll('Sarah','F')
print(a)
#与默认参数不服提供额外信息
a=enroll('Bob','M',7)
print(a)
print(enroll('Adam','M',city='Tianjin'))

def add_end(L=[]):
    L.append('END')
    return L
print(add_end([1,2,3]))
print(add_end(['x','y','z']))

print(add_end())
print(add_end()) #['END', 'END']
print(add_end()) #['END', 'END', 'END']
#设计不变对象，返回['END']
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
print(add_end())
print(add_end())



