import requests
url = 'http://zenon.net'
par = {'key1':'value1','key2':'value2'}
r = requests.get(url, params=par)
print(r.url)
