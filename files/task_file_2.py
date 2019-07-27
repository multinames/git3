s =''
l = {}
with  open ('dataset_3363_3.txt') as inf:
    for line in inf:
        line = line.strip()
        s += line
#print(s)

for i in s.split():
	if i in l:
		l[i] += 1
	else:
		l[i] = 1
#print (l)

#print({l[k]: k for k in l})
#print(dict(reversed(item) for item in l.items()))
#print (l.values())

#for i in l.values():
#	print (i)

count=0
for key,value in l.items() :
    if value>count :
        z=key
        x=value
        count=x
    else :
        continue
print(z,x)