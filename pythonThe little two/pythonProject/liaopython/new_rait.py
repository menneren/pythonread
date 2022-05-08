'''*args是可变参数，args接收的是一个tuple；

**kw是关键字参数，kw接收的是一个dict。'''


def mul(*num):
    # print('len的长度：'，len(num))
    if len(num)==0:
        raise TypeError
    else:
        res=1
        for x in num:
            res=res*x
        return res

print('mul(5) =', mul(5))
print('mul(5, 6) =', mul(5, 6))
print('mul(5, 6, 7) =', mul(5, 6, 7))
print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
if mul(5) != 5:
    print('测试失败!')
elif mul(5, 6) != 30:
    print('测试失败!')
elif mul(5, 6, 7) != 210:
    print('测试失败!')
elif mul(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        mul()
        print('测试失败!')
    except TypeError:
        print('测试成功!')

