objects = [1, 2, 1, 2, 3]
a = set()
ans = 0
for obj in objects: # доступная переменная objects
    a.add(id(objects[ans]))
    ans += 1
print(len(a))

