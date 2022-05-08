from pathlib import Path
A = Path.cwd()
print(A)


p = Path('/Users/liujiyang/PY/pythonThe little turtle/储存')
print(p)
#路径连接
q = p / "FishC.txt"
print(q)

#用dir判断是否是文件夹
T = p.is_dir()
print(T)   #True

T = q.is_dir()
print(T)   #False

T = p.is_file()
print(T)   #False

T = q.is_file()
print(T)

#判断路径是否正确
T = p.exists()
print(T)

T = q.exists()
print(T)


T = Path("C:/404").exists()
print(T)

T = p.name
print(T)
T = q.name
print(T)
#获取文件名
T = q.stem
print(T)
T = p.stem
print(T)
#获取文件后缀
T = q.suffix
print(T)
T = p.suffix
print(T)

#获取父级目录
T = p.parent
print(T)

t = q.parent
print(t)

#获取逻辑祖先路径构成的序列
p.parents
ps = p.parents
for each in ps:
    print(each)

print(ps[0])
print(ps[1])
print(ps[2])

#parts将路径的各个组件分成元组
T = p.parts
print(T)

#stat()查询文件或文件夹的信息
T = p.parts
print(T)

#文件夹的尺寸
T = p.stat().st_size
print(T)

T = q.stat().st_size
print(T)

#p和q是绝对路径
p = Path("./doc")
print(p)

p = Path("../FishC")
print(p)

#相对路径
p = Path("./doc").resolve()   #resolve()将相对路径转换为绝对路径
print(p)

p=Path("../FishC").resolve()
print(p)

#iterdir文件和文件夹对象打印出来
p = p.iterdir()
print(p)
'''
for each in p.iterdir():
    print(each)
'''

#列表推导式
#[x for x in p.iterdir() if x.is_file()]

'''
n = p / "FishC"
n.mkdir()


n.mkdir(exist_ok=True)
'''


n = p/"FishC/A/B/C"
n.mkdir(exist_ok=True)

n.mkdir(parents=True, exist_ok=True)


n = n /"FishC.txt"
print(n)

f = n.open("w")
f.write("I love FishC.")

f.close()
n.rename("NewFishC.txt")

m = Path("NewFishC.txt")
print(m)

m.replace(n)

#n.parent.redir()

n.unlink()

n.parent.redir()

p.glob("*.txt")

list(p.glob("*/*.py"))


list(p.glob("**/*.py"))

#删除文件夹



#查找文件


