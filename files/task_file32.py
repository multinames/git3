l = {}
with  open ('dataset_3363_4.txt') as inf:
   for a in inf :
    a = a.strip().split(';')
    #print(a[1:])
    l[a[0]]= a[1:]
print(l)