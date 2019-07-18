b = []
while True:
    a = [i for i in input().split()]
    if a[0] == 'end':  break
    b += [a]
 #вывод
for i in range(len(b)):
    for j in range(len(b)):
        print(b[i][j], end=' ')
    print()