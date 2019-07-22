def min(*a):
    m = a [0]
    for x in a:
        if m > x:
            m = x
    return m

n = min(5,3,6,10)
print (n)
