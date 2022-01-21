def sum_arguments(*args):
	sum = 0
	i = 0
	for elem in args:
		sum += elem * i
		i += 1
	return sum
print(f'Сумма аргументов умноженное на индекс равно:{sum_arguments(*args)}')