n = int(input())
i = 0
b = dict()
while i < n :
    j = 0
    a = [i for i in input().split(';')]
    while j < len(a):
        #print(a[j])
        if a[j].isalpha() == True:
            print ('Команда :', a[j])
            j += 1
        else:

            print(a[j])

            j += 1
    i+=1



