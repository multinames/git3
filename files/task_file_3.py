l = []
d = dict()
#i = 0
s = 0
with  open ('dataset_3363_4.txt') as inf:
   for a in inf :
    a = a.strip().split(';')
    l +=a
    #print(a)
print(l)
for i in l:
    #print(s)
    if i.isalpha() != True:
        print(i)
