result = ''
with open('task1.txt') as inf:
	line = inf.readline()
	i = 1
	while i < len(line):
		# вводим переменную для хранения чисел в виде строк (для двух- и более значных чисел)
		m = ''
		# заводим счетчик
		n = 1
		while i < len(line) and line[i] in '0123456789':
			# если число, то прибавляем к переменной m и увеличтваем счетчик
			m += line[i]
			n += 1
			i += 1
		result += line[i-n]*int(m)
		i += 1
print (result)
with open('outfile.txt', 'w') as ouf:
	ouf.write(result)
