def update_dictionary(d, key, value):
    if key in d.keys():
        d[key] += [value]
    elif 2*key not in d.keys():
        d[2*key] = [value]
    elif key not in d.keys():
        d[2*key] += [value]


d = {}
print(update_dictionary(d, 1, -1))
print(d)
update_dictionary(d, 2, -2)
print(d)
update_dictionary(d, 1, -3)
print(d)