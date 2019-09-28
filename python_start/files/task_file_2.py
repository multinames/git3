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
print (l)

#for i in sorted(l):
#	print (i,l[i])
