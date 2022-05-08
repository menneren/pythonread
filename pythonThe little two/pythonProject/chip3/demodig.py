num_a=input('请输入第一个整数')
num_b=input('请输入第二个整数')
'''
if num_a>=num_b:
    print(num_a,'大于等于',num_b)
else:
    print(num_a,'小于',num_b)
'''

print('使用条件表达式进入比较')
#条件判断正确执行左侧，不通过执行else
print( str(num_a)+'大于等于'+str(num_b) if num_a>=num_b else str(num_a)+'小于'+str(num_b) )




