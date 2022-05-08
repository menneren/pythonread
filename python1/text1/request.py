import requests

url = "https://www.baidu.com"

params = {
    "qrant_type":"u",
    "appid":"c470d03db594"
}

res = requests.get(url=url, params=params)
print(res.json())       #把返回值转化成一个dict对象
print(res.text)         #把返回值转化成文本
print(res.content)      #把返回值转化成字节类型数据
print(res.status_code)  #返回码
print(res.reason)       #返回信息
print(res.cookies)      #返回cookie信息
print(res.encoding)     #编码格式



