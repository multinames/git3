#with  open ('task1.txt') as inf:
#   for line in inf:
line ='n7b4z6t20S6u16q15h4P1e5n3f12k1Y20B15v20i14P11a15m8r10m19S10h7N3w15a12X13v18I3F17r6J20H16J16d8x13k18D12B9I3F4d2o12f15H16W3'
      # line = line.strip()
#print(line)
i = 0
#j = 0
s =''
d = dict()

while i < len(line):
    if line[i].isdigit() == True and line[i-1].isdigit() == True:
            print (line[i-1]+line[i],end=' ')
    elif line[i].isdigit() == True and line[i+1].isdigit() != True:
            print(line[i], end=' ')
    #elif line[i].isdigit() != True:
     #       print(line[i], end=' ')


    i+=1
    #print(d)


