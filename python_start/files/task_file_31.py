#f = open('dataset_3363_4.txt')
with open("dataset_3363_4.txt", "r") as my_file:
    str = my_file.read()
#print(str)
#print(type(str))

for i in str.split(';'):
     print (i, end =' ')


