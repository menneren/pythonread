#打开写入
f=open("FishC.txt","w")

#写入
f.write("I love Python.")
print(f)
#<_io.TextIOWrapper name='FishC.txt' mode='w' encoding='UTF-8'>


#写入换行
f.writelines(["I love FishC.\n", "I love my wife."])
print(f)

f=open("FishC.txt", "r+")
print(f.readable())

print(f.writable())

for each in f:
    print(each)

print(f.read())
#文件指针，字符数
print(f.tell())
#文件指针到文件开头
print(f.seek(0))
#读取第一行内容
print(f.readline())
#再次运行读取第二行
#f.readline()

print(f.read())

print(f.write("I love my WIFI."))

#截取文件
f.flush()
A=f.truncate(29)
print(A)

#清除
'''f.close()
f=open("FishC.txt","w")
f.close()
'''

