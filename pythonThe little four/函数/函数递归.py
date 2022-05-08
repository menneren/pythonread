def funA():
    print("AMBDYL") #打印

def funB():
    funA()

funB()

def funC():
    print("AMBDYL")
    funC()

#funC()

def funC(i):
    if i>0:
        print("AMBDYL")
        i-=1
        funC(i)

funC(10)

#for循环
def factlter(n):
    result = n
    for i in range(1, n):
            result *= i
    return result

print(factlter(5))
print(factlter(10))

#递归
def factRecur(n):
    if n == 1:
        return 1
    else:
        return n * factRecur(n-1)

print(factRecur(5))

def fibIter(n):
    a=1
    b=1
    c=1
    while n>2:
        c=a+b
        a=b
        b=c
        n-=1
    return c

print(fibIter(12))

#递归耗费资源
def fibRecur(n):
    if n==1 or n==2:
        return 1
    else:
        return fibRecur(n-1) + fibRecur(n-2)
print(fibRecur(12))
#print(fibRecur(120))

print(fibIter(120))



