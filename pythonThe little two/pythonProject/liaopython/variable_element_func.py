#可变参数
def calc(numbers):
    sum = 0
    for n in numbers:
        sum=sum+n*n
    return sum

print(calc([1,2,3]))
print(calc((1,3,5,7)))


def calc(*numbers):
    sum=0
    for n in numbers:
        sum=sum+n*n
    return sum

print(calc(1,2))
print(calc())

print(calc(1,2,3))
print(calc(1,3,5,7))

def person(name,age,**kw):
    print('name',name,'age',age,'other:',kw)

print(person('Micheal',30))

print(person('Bob',35,city='Beijing'))

print(person('Adam', 45, gender='M', job='Engineer'))

extra={'city':'Beijing','job':'Engineer'}
person('Jack',24,**extra)

def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)

print(person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456))


def person(name, age, *, city, job):
    print(name, age, city, job)
print(person('Jack',24,city='Beijing',job='Engineer'))

def person(name, age, *args, city, job):
    print(name, age, args, city, job)
#缺少参数名报错
#print(person('Jack', 24, 'Beijing', 'Engineer'))

def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)
print(person('Jack', 24, job='Engineer'))

def person(name, age, city, job):
    # 缺少 *，city和job被视为位置参数
    pass

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

print(f1(1, 2))
print(f1(1, 2, c=3))
print(f1(1, 2, 3, 'a', 'b'))
print(f1(1, 2, 3, 'a', 'b', x=99))
print(f2(1, 2, d=99, ext=None))

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}

print(f1(*args, **kw))

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
print(f2(*args, **kw))

