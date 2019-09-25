sp = []
with open('dataset_3363_3.txt') as f:
    for s in f:
        s = s.strip().lower()
        for ss in s.split():
            sp.append(ss)
count = 0
print (sp)
for elem in sp:
    if sp.count(elem) > count:
        count = sp.count(elem)
        slovo = elem
print(slovo, count)