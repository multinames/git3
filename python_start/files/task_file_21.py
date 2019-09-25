s =''
a = ''
l = {}
with  open ('dataset_3363_3.txt') as inf:
    for line in inf:
        line = line.strip()
        s += line
#print(s)
a = s.split(' ')
#print (a)

#print (a.count('ZaaZ'))

for i in s.split():
    #print(i)
    print(a.count(i))
#for i in s.split():
#	if i in l:
#		l[i] += 1
#	else:
#		l[i] = 1
#print (l)