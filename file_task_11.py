#with  open ('task1.txt') as inf:
#   for line in inf:
line ='n7b4z6t20S6u16q15h4P1e5n3f12'
      # line = line.strip()
#print(line)
i = 0
j = 0
s =''
d = dict()

while i < len(line):
    if line[i].isdigit() == True and line[i-1].isdigit() == True:
            s += (line[i - 1] + line[i])
            #print (line[i-1]+line[i], end= ' ')
            print(line[i - 1] + line[i], end=' ')
            i+=1
    elif line[i].isdigit() == True and line[i+1].isdigit() != True:
        j=0
        s += (line[i])
        print(line[i], end= ' ')

    elif line[i].isalpha() == True:
        j = 0
        s +=line[i]
        print(line[i], end= ' ')
        d[line[i]]= 0
    i+=1

print(s)


