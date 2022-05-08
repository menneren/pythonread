help(print)

#函数文档
def exchange(dollar, rate=6.32):
    """
    功能；汇率转换，美元 -> 人民币
    参数：
    - dollar 美元数量
    - rate 汇率，默认值是 6.32(2022-03-08)
    返回值：
    - 人民币的数量
    :param dollar:
    :param rate:
    :return:
    """
    return dollar * rate

print(exchange(20))

def exchange(dollar, rate=6.32):
    """
    :param dollar:
    :param rate:6.32
    :return:
    """
    return dollar * rate
print(exchange(20))

#类型注释
def times(s:str, n:int) -> str:
    return s * n
print(times("FishC",5))
print(times(5,5))

def times(s:str = "FishC", n:int = 3) -> str:
    return s * n
print(times())

def times(s:list, n:int = 3) -> list:
    return s * n
print(times([1,2,3]))

def times(s:list[int], n:int = 3) -> list:
    return s*n

def times(s:dict[str, int], n:int = 3) -> list:
    return list(s.keys()) * n
print(times({'A':1,'B':2,'C':3}))

#用python检测用第三方模块Mypy

#内省
times.__name__      #times

times.__annotations__
print(times.__annotations__)

exchange.__doc__
print(exchange.__doc__)   #print转译字符




