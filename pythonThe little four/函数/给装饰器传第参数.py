import time
def logger(msg):
    def time_master(func):
        def call_func():
            start = time.time()
            func()
            stop = time.time()
            print(f"[{msg}]一共耗费了{(stop-start):.2f}")
        return call_func
    return time_master

#@logger(msg="A")
def funA():
    time.sleep(1)
    print("正在调用funA...")

#@logger(msg="B")
def funB():
    time.sleep(1)
    print("正在调用funB...")
#调用将参数传递出去
funA = logger(msg="A")(funA)
funB = logger(msg="B")(funB)

funA()
funB()



