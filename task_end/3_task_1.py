n = int(input())
i = 0
b = dict()
c = []
#Команда:Всего_игр Побед Ничьих Поражений Всего_очков
#За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
while i < n :
    j = 0
    a = [i for i in input().split(';')]
    while j < len(a):
        #print(a[j])
        if a[j].isalpha() == True:
            #print ('Команда :', a[j])
            b[a[j]] = [0,0,0,0,0]
            j += 1
        else:

            #print(a[j])

            j += 1
    i+=1
print (b)


