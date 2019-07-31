import requests
dir='https://stepic.org/media/attachments/course67/3.6.3/'
with open('dataset_3378_3.txt', 'r') as inf:
        url = inf.readline()
#        print('Start URL',url)
while True:
        r = requests.get(url.strip())
        if r.text[0:2] == "We":
                print (r.text)
                break
        url = dir+r.text
#        print (r.text)
#        print(url)



