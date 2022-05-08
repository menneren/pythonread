#lambda  arg1,arg2,arg3,....argN :expression
#关键字   传入函数参数  ：  表达式/返回值

#平方
def squareX(x):
    return x*x


'''got an unexpected keyword argument 'msg'
squareX()得到一个意想不到的关键字参数'msg'''
#squareX=squareX(msg="X")(squareX)     #logger(msg="A")(funA)

t=squareX(3)
print(t)


squareY = lambda y : y*y
squareY(3)

t=squareX
print(t)

squareY

#字典
y=[lambda x : x*x,2,3]
t=y[0](y[1])    #(y[1)参数
print(t)

y[0](y[2])

mapped = map(lambda x:ord(x) + 10,"FishC")

A = list(mapped)
print(A)

def boring(x):
    return ord(x) + 10

B = list(map(boring,"FishC"))
print(B)

BB=list(filter(lambda x:x%2,range(10)))
print(BB)



