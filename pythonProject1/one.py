import requests

rep = requests.request()

print(rep.text)

print(rep.content)