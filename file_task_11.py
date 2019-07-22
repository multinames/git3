#with  open ('task1.txt') as inf:
#   for line in inf:
line ='n7b4z6t20S6u16q15h4P1e5n3f12'
      # line = line.strip()
#print(line)
i = 0
#j = 0
s =''
d = dict()
#line1 = line[i::-1]
while i < len(line):
    #print(line[i], end ='')
    if line[i].isdigit() != True:
        print(line[i])
            #if line[:i+1].isdigit() == True:
             #   print(line[:i+1])
        i += 1
    else:
        #print(line[i])
        i += 1
        #d[line[i]] = i
    #i += 1
        #print (line[i:-1].lower())
        #print (line[i], line[i].isdigit())
        #print (line[i])
#i += 1
print (line)
#print (d)