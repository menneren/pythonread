import time

def time_master(func):
    def call_func():
        print("开始运行程序...")
        start = time.time()
        func()
        stop = time.time()
        print("结束程序运行...")
        print(f"一共耗费了{(stop-start):.2f}秒。")
    return call_func

def myfunc():
    time.sleep(2)
    print("I love FishC.")

myfunc = time_master(myfunc)
myfunc()

#functool
def add(x, y):
    return x+y

import functools
A=functools.reduce(add,[1,2,3,4,5])
print(A)

A=add(add(add(add(1,2),3),4),5)
print(A)

#10的阶乘
A=functools.reduce(lambda x,y:x*y, range(1,11))
print(A)

T=lambda x,y:x*y, range(1,11)
print(T)

#偏函数
square = functools.partial(pow,exp=2)
print(square(2))
print(square(3))

cube = functools.partial(pow, exp=3)
print(cube(2))
print(cube(3))


print(myfunc.__name__)   #call_func




