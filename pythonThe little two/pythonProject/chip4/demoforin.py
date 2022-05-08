for item in 'Python':
    print(item)

for i in range(10):
    print(i)
#如果循环中不需要使用到自定义变量，可将自定义变量写为"_"
for _ in range(5):
    print(' 人生苦短，我用Python')

print('使用for循环，计算1到100之间的偶数和')
sum=0
for item in range(1,101):
    if item %2==0:
        sum+=item

print('1到100之间的偶数和为：',sum)


