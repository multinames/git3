d = dict()
s, s2 , s3 = 0, 0, 0
with  open ('dataset_3363_4.txt') as inf:
   for a in inf :
    a = a.strip().split(';')
    d[a[0]] = [int(a[1]),int(a[2]),int(a[3])]
with open('outfile.txt', 'w') as ouf:
    for value in d.values():
        ouf.write(str(sum(value)/3)+'\n')
        s += value[0]
        s2 += value[1]
        s3 += value[2]
    ouf.write (str(s/(len(d))) +' '+ str(s2/(len(d))) + ' '+str(s3/(len(d))))

