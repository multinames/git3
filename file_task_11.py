#with  open ('task1.txt') as inf:
#   for line in inf:
line ='n7b4z6t20'
       #line = line.strip()
       #print (line)
i = 0
s =''
d = dict()
while i < len(line):
    #print(line[i], end ='')
    if line[i].isdigit() == True:
            #print(line[i],line[i:i+2],'i=',i, end= ' ')
            print(line[i],i)
            #s += str(line[i])
            #if line[i:i+1].isdigit() == True:
            #         print ('Два')
            i += 1
    else:

        print(line[i],i)
        i += 1
        #d[line[i]] = i

        #print (line[i:-1].lower())
        #print (line[i], line[i].isdigit())
        #print (line[i])
#i += 1
#print ()
#print (d)