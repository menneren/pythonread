print("小甲鱼")

print("小甲鱼","爱","编程")

def myfunc(*args):
    print("有{}个参数，".format(len(args)))
    print("第2个参数是：{}".format(args[1]))

myfunc("小甲鱼","不二如是")

myfunc(1,2,3,4,5)

def myfunc(*args):
    print(args)
myfunc(1,2,3,4,5,6)

def myfunc():
    return 1,2,3
print(myfunc())

x,y,z=myfunc()
print(x)
print(y)
print(z)

def myfunc(*args):
    print(type(args))
myfunc(1,2,3,4,5)

def myfunc(*args,a,b):
    print(args,a,b)

#myfunc(1,2,3,4,6)  关键字参数只能放在位置参数后面
myfunc(1,2,3,a=4,b=5)

def abc(a,*,b,c):
    print(a,b,c)
#abc(1,2,3)    关键字参数报错
abc(1,b=2,c=3)

def myfunc(**kwargs):
    print(kwargs)
myfunc(a=1,b=2,c=3)
#{'a': 1, 'b': 2, 'c': 3}  关键字参数

def myfunc(a,*b,**c):
    print(a,b,c)
myfunc(1,2,3,4,x=5,y=6)

help(str.format)
'''Help on method_descriptor:

format(...)
    S.format(*args, **kwargs) -> str
    
    Return a formatted version of S, using substitutions from args and kwargs.
    The substitutions are identified by braces ('{' and '}').
'''

args=(1,2,3,4)
def myfunc(a,b,c,d):
    print(a,b,c,d)
#myfunc(args)

myfunc(*args)

kwargs={'a':1,'b':2,'c':3,'d':4}
myfunc(**kwargs)








