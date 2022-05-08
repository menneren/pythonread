#函数的返回值
def myfunc():
    print("正在调用myfunc....")

#函数调用函数
def report(func):
    print("主人，我要开始调用函数了...")
    func()
    print("主人，我调用完函数啦，快夸夸我^o^")

report(myfunc)

#程序运行所用时间⌚️
import time
def time_master(func):
    print("开始运行程序...")
    start = time.time()
    func()
    stop = time.time()
    print("结束程序运行...")
    print(f"一共耗费了{(stop-start):.2f}秒。")

def myfunc():
    time.sleep(2)
    print("hello Fishc.")

time_master(myfunc)











