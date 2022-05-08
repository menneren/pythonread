#with语句和上下文管理器
f = open("FishC.txt","w")
f.write("I love FishC.")    #写入

f.close()    #关闭

#上下文管理器(保证文件顺利存储)
with open("FishC.txt","w") as f:
    f.write("I love FishC.")


import pickle

x,y,z,=1,2,3
s="FishC"
l={"小甲鱼",520,3.14}
d={"one":1,"two":2}
'''
with open("data.pkl","wb") as f:
    pickle.dump(x, f)
    pickle.dump(y, f)
    pickle.dump(z, f)
    pickle.dump(s, f)
    pickle.dump(l, f)
    pickle.dump(d, f)
'''
with open("data.pkl","wb") as f:
    pickle.dump((x, y, z, s, l, d), f)






