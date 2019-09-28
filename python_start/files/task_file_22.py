string = str()
with open('dataset_3363_3.txt') as data:
    for line in data:
        string += line.strip()

string = string.upper().split()
comparison_set = set(string)
dic_set = {}
for i in comparison_set:
    if string.count(i) in dic_set:
        dic_set.get(string.count(i)).append(i)
        continue
    dic_set[string.count(i)] = [i]

with open('outputData.txt', 'w') as data:
    k = max(dic_set)
    for i in sorted(dic_set.get(k)):
        data.write(i + ' ' + str(k) + '\n')