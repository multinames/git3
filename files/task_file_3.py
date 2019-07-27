l = []
d = dict()
#i = 0
s = 0
with  open ('dataset_3363_4.txt') as inf:
   for a in inf :
    a = a.strip().split(';')
    l +=a
    #print(a)
#print(l)
d['marks'] = []
for i in l:
    #print(s)
    if i.isalpha() == True:
        d['name'] = i
        print(i)
        print(d)
        #print(s)
        #s = 0
    #else:
     #   while i.isdigit() == True:

    elif i.isdigit() == True:

        #s += int(i)
        d['marks'].append(int(i))
        print(i)
            #s += int(i)

            #break
        #print(s)




#l = {}
#[print(el) for el in a]

#for el in a:
#    print(el)
#for i in line:
#	if i in l:
#		l[i] += 1
#	else:
#		l[i] = 1
