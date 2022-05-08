def counter():
    i = 0
    while i <= 5:
        yield i
        i += 1

p = counter()
print(p)

for i in counter():
    print(i)
c=counter()   #c就是generator object
print(c)

#每调用一次获得一个结果
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
#print(next(c))

'''
#无法用下标所引获得返回值
c = counter()
print(c[2])'''

#每个数据都是前一个数据的和
def fib():
    back1, back2 = 0, 1
    while True:
        yield back1
        back1, back2 = back2, back1 + back2

f = fib()
A = next(f)
print(A)

A = next(f)
print(A)

A = next(f)
print(A)

A = next(f)
print(A)

A = next(f)
print(A)

A = next(f)
print(A)

'''for i in f:
    print(i)
'''


(i**2 for i in range(10))

t=(i**2 for i in range(10))
print(next(t))

print(next(t))

print(next(t))

print(next(t))

print(next(t))

print(next(t))

for i in t:
    print(i)
