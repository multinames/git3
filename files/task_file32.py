l = []
i = 0
s = 0
with  open ('dataset_3363_4.txt') as inf:
   for a in inf :
    a = a.strip().split(';')
    #if a.isalpha() == True:
    l += a[1:]
    #l[a[0]]= a[1:]
    #i += 1
#print(l)
#print(len(l))

while i < len(l):
#    print (l[i])
    s += int(l[i])
    i+=1
print(s)