r=range(10)    #[0，1，2，3，4，5，6，7，8，9]，默认从0开始，默认相差1称为步长
print(r)     #range(0,10)
print(list(r))  #用于查看range对象中的整数序列   -->list是列表的意思

'''第二种创建方式，给了两个参数（小括号中给了两个数）'''
r=range(1,10)
print(list(r))     #[1,2,3,4,5,6,7,8,9]

'''第三种创建方式，给了三个参数（小括号中给了三个数）'''
r=range(1,10,2)
print(list(r))   #[1,3,5,7,9]

'''判断指定的整数  在序列中是否存在 in，not in'''
print(10 in r)    #False,10不在当前的r这个整数序列中
print(9 in r)     #True,9在当关的r这个序列中

print(10 not in r)
print(9 not in r)

print(range(1,20,1))   #[1...19]
print(range(1,101,1))  #[1....100]


