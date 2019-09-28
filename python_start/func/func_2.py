lst = [1, 2, 3, 4, 5, 6]

def modify_list(l):
    i=0
    while i < len(l):
        b = []
        if (l[i]%2) == 0 :
            b.append(l[i]/2)
            i+=1
        else:
            l.remove(l[i])


print(modify_list(lst))
