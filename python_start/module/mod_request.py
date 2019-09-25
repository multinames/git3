import requests

r = requests.get('http://zenon.net')
print(r.text)

url = 'http://zenon.net'
par = {'key1':'value1','key2':'value2'}
r = requests.get(url, params=par)
print(r.url)
