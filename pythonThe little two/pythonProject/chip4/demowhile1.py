#print(bool(0))
sum=0
a=1
while a<=100:
    if not bool(a%2):
        sum+=a
        print(sum)
    a+=1
print('1-100之间的偶数和',sum)