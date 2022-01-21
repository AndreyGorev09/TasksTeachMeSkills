import random
a = int(input('Введите размер матрицы от 1 до n: '))
b = int(input('Введите дипозон случайных чисел от: '))
c = int(input('Введите дипозон случайных чисел до: '))
sum = 0
for i in range(a*a):
    x = random.randint(b, c)
    print(x)
    if x % 3:
        continue
    else:
        sum += x
print(f'Сумма всех элементов матрицы, кратные "3": {sum}')