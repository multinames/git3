import requests
url = 'https://stepic.org/media/attachments/course67/3.6.2/289.txt'
r = requests.get(url.strip())
print(len(r.text.splitlines()))
