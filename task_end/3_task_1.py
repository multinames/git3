n = int(input())
i = 0
b = dict()
c = []
ag = 0
#Команда:Всего_игр Побед Ничьих Поражений Всего_очков
#За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
while i < n :
    j = 0
    a = [i for i in input().split(';')]
    while j < len(a):
        print(a[j])
        if a[j].isalpha() == True:
            b[a[j]] = [0,0,0,0,0]
            #print(b)
            j += 1
        else:

            #print(a[j])

            j += 1
    i+=1
print (b)


