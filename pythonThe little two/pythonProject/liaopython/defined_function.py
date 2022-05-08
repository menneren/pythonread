#启用python解释器
from abstest import my_abs
print(my_abs(-10))

#空函数，占位
def nop():
    pass

#其他语句pass
a=1
if a>=18:
    pass

#参数个数不对
#my_abs(1, 2)
#参数类型不对，报错
#my_abs('A')
#abs('A')

#数据类型检查内置函数isinstance()
import math

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

n = my_abs(-20)
print(n)

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

r = move(100, 100, 60, math.pi / 6)
print(r)

# TypeError: bad operand type:
#my_abs('123')



