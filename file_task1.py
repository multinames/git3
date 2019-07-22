with  open ('task1.txt') as inf:
   for line in inf:
       line = line.strip()
#       print(line, end='')
#       print()
#line ='n7b4z6t20S6u16q15h4P1e5n3f12k1Y20B15v20i14P11a15m8r10m19S10h7N3w15a12X13v18I3F17r6J20H16J16d8x13k18D12B9I3F4d2o12f15H16W3'

d = dict()
d1 = dict()
s = ''
s1 = ''
#while i < len(line):
for i in line.lower():
        #if i.isalpha() == True:
        if i.isdigit() == True:
            print (i, end='')
            print(i, end='')



            s += i

        #elif i.isalpha() == False:
         #   print(s, i * int(i))



        #else:
            #print (int(i), end='')
         #s1 = s *int(i)
         #print (s,i*int(i))


#print(s)
#print(s1)
