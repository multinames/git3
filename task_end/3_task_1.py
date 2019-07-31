n = int(input())
i = 0
b = dict()
while i < n :
    a = [i for i in input().split(';')]
    print (a[1])
    if a[1] in b:
        #b[0] = +a[0]
        print (a[3])
        print ('Yes')
    else:
        print('No')
        #print(a)
    b[a[0]] = a[1]
    print(b)
    i+=1


