line ='n7b4z6t20S6u16q15h4P1e5n3f12k1Y20B15v20i14P11a15m8r10m19S10h7N3w15a12X13v18I3F17r6J20H16J16d8x13k18D12B9I3F4d2o12f15H16W3'
l = len(line)
n = [] #строка накопления
i = 0 #счетчик
while i < l: #общий цикл
    s_int = '' #промежуточная строка накопления, обнуляется
    a = line[i] # промежуточная переменна, присваивается
    while a.isdigit() == True : #цикл на проверку цифра или нет.
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