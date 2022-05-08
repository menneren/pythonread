def hanoi(n, x, y, z):
    if n == 1:
        print(x, '-->',z)   #如果只有1层，直接将金片从x移动到z
    else:
        hanoi(n-1, x, z, y)  #将x上的n-1个金片移动到y
        print(x, '-->', z)   #将最底下的金片从x移动到z
        hanoi(n-1, y, x, z)  #将y上的n-1个金片移动到z

n = int(input("请输入汉洛塔的层数："))
hanoi(n,'A','B','C')














