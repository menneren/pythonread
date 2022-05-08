def myfunc(o, vt, s):
    return "".join((o, vt, s))#join是str型只能有一个函数

print(myfunc("我","打了","美少女"))

print(myfunc("美少女","打了","我"))

t=myfunc(o="我",vt="打我",s="美少女")#关键字参数
print(t)

#myfunc(o="我","打我","美少女")
#SyntaxError: positional argument follows keyword argument

def myfunc(s,vt,o="小酒鱼"):   #默认参数
    return "".join((o,vt,s))

t=myfunc("香蕉","吃")
print(t)
t=myfunc("香蕉","吃","不二如是")
print(t)

'''def myfunc(s="苹果",vt,o="小甲鱼"):
    return "".join(o,vt,s)'''
#non-default argument follows default argument
#非默认参数紧跟在默认参数之后

def myfunc(vt,s="苹果",o="小甲鱼"):
    return "".join((o,vt,s))

t=myfunc("拱了")
print(t)

help(abs)
#abs(x, /)斜杠左侧不能使用关键字参数，只能使用位置参数
print(abs(-1.5))

print(sum([1,2,3],4))
print(sum([1,2,3],start=4))

def abc(a,/,b,c):
    print(a,b,c)

abc(1,2,3)
#abc(a=1,2,3)
#左边不能用关键字

abc(3,b=2,c=3)

def abc(a,*,b,c):  #*后必须用关键字参数
    print(a,b,c)

abc(1,b=2,c=3)
abc(a=1,b=2,c=3)












