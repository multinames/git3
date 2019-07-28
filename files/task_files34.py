l = []
i = 0
s = 0
n = 4
with  open ('dataset_3363_4.txt') as inf:
   for a in inf :
    a = a.strip().split(';')
    #if a.isalpha() == True:
    s = int(a[1]) + int(a[2])+int(a[3])
    print(a[0],s/3)

#a = [[0] * n] * n
#print(a)
#a[0][0] = 5
#print(a)