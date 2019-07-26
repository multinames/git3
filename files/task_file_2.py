s =''
d = dict()
i = 1
with  open ('dataset_3363_3.txt') as inf:
    for line in inf:
        line = line.strip()
        s += line.lower()
print(s)


for i in s:
    #print(i)
    if i in d:
        d[i] =+1
    else:
        d[i] = 1
print (d)