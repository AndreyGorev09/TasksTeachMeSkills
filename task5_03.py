import random
n = int(input('Введите размер матрицы от 1 до n: '))
m = int(input('Введите размер матрицы от 1 до m: '))
c = int(input('Введите дипозон случайных чисел от: '))
d = int(input('Введите дипозон случайных чисел до: '))
count = 0
for i in range(n*m):
    x = random.randint(c, d)
    print(x)
    if x != 7:
        continue
    else:
        count += 1
print(f'Количество чисел равных "7" равно:{count}')