def factorial(n):
	if n == 0:
		return 1
	return factorial(n-1) * n
n = int(input('Введите число для нахождения факториала: ')
print(f' Факториал {n} равен: {factorial(n)}')