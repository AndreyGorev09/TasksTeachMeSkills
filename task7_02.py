# Написать программу для работы с матрицами:
# 1. Создание
# 2. Вывод
# 3. Сумма всех элементов
# 4. Нахождение максимального элемента
# 5. Нахождение минимального элемента.

import random
def job_matrix(matrix_str, matrix_stolb, random_int_from, random_int_to):
    m = {}
    for i in range(matrix_str):
        for j in range(matrix_stolb):
            m[i, j] = (random.randint(random_int_from, random_int_to))
    print(m)

    matrix_sum = sum(m.values())
    print(f'{matrix_sum}')

    matrix_max_element = max(m.values())
    print(f'{matrix_max_element}')

    matrix_min_element = min(m.values())
    print(f'{matrix_min_element}')
print(job_matrix(3,3,2,7))