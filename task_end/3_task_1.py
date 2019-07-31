n = int(input())
i = 0
b = []
while i < n :
    a = [i for i in input().split()]
    print(a)
    b += a
    i+=1
print(b)
