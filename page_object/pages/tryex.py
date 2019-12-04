try:
    print(2/0)
except ValueError:
    print("ValueError")
else:
    print("else")
finally:
    print("Даже если в конструкции ошибка то вывод будет.")
