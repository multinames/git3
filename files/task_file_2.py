s =''
l = ''
d = dict()
i = 1
with  open ('dataset_3363_3.txt') as inf:
    for line in inf:
        line = line.strip()
        s += line
#print(s)
#print(s.split())
#print(s)

z = {}
for i in s.split():
	if i in z:
		z[i] += 1
	else:
		z[i] = 1
print (z)