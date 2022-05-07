import requests

rep = requests.request()

#返回字符串的数据
print(rep.text)
#返回字节格式的数据
print(rep.content)
#返回字典格式的数据
print(rep.json())


