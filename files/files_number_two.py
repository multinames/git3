line ='n7b4z6t20S6u16q15h4P1e5n3f12k1Y20B15v20i14P11a15m8r10m19S10h7N3w15a12X13v18I3F17r6J20H16J16d8x13k18D12B9I3F4d2o12f15H16W3'
l = len(line)
n = []
i = 0
while i < l:
    s_int = ''
    a = line[i]
    while a.isdigit() == True :
        s_int += a
        i += 1
        if i < l:
            a = line[i]
        else:
            break
    i += 1
    if s_int != '':
        n.append(int(s_int))

print(n)