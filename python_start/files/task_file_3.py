l = []
with  open ('dataset_3363_4.txt') as inf:
   for a in inf :
    a = a.strip().split(';')
    l += a
print(l)
count, s = 0, 0
for i in l:
    if i.isdigit() == True:
            #print(i, end=' ')
            s += int(i)
            count += 1
            if count == 3:
             #   print()
                print(s/3)
                count = 0
                s = 0


