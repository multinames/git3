with  open ('task1.txt') as inf:
   for line in inf:
    line = line.strip()
i, j, n, m = 0, 1, 0 ,0
s = ''
d = []
while i < len(line):
    if line[i:j].isdigit() == True and line[i+1:j+1].isdigit() == True:
        d.append (line[i]+line[i+1:j+1])
    elif line[i:j].isdigit() == True and line[i-1:j-1].isalpha() == True:
        d.append(line[i])
    elif line[i:j].isalpha() == True:
        d.append(line[i:j])
    i += 1
    j += 1
while n < len(d):
    if d[n].isalpha() == True:
        s += d[n]*(int(d[n+1]))
    n+=1
print (s)
with open ('input.txt','w') as ouf:
    ouf.write (s)
