'''import math
a=math.sqrt(2)
print(a)'''

# -*- coding: utf-8 -*-

import math

def quadratic(a, b, c):
    m=b*b-4*a*c
    if m>=0:
        x=(-b+math.sqrt(m))/(2*a)
        y=(-b-math.sqrt(m))/(2*a)
        return x,y
    else:
        return 'no answer!'
print(quadratic(2,3,1))
print(quadratic(1,3,1))
print(quadratic(1,4,4))
print(quadratic(1,-4,4))

# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')


