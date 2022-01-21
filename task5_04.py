import random
n = int(input('Введите размер матрицы от 1 до n: '))
m = int(input('Введите размер матрицы от 1 до m: '))
c = int(input('Введите дипозон случайных чисел от: '))
d = int(input('Введите дипозон случайных чисел до: '))
matrix = {}
sum = 0
for x in range(n):
    for y in range(m):
        matrix[x, y] = random.randint(c, d)
        sum += matrix[x, y]
        print(matrix[x, y], end=' ')
    print('\n')
averange_value = (int(sum) / (len(matrix)))
count = 0
for x in range(n):
    for y in range(m):
        if matrix[x, y] > averange_value and (x + y)%2 == 0:
            count += 1
            print(f'Значение подходящее под условие: {matrix[x, y]}')
print(f'Среднее значение элементов {averange_value}, количество элементов соответствующие условию {matrix[x, y]}')
