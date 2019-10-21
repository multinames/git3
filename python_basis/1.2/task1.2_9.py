objects = [1, 2, 1, 2, 3]

ans = 0
for obj in objects: # доступная переменная objects
    print(id(objects[ans]))
    ans += 1
print(ans)
