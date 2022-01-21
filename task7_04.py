# Реализовать функцию возвращающую матрицу. На вход принимает n - размерность матрицы,
# random_from(по-умолчанию 1),
# random_to(по-умолчанию(9)).
import random
def matrix(n):
    m = {}
    for i in range(n):
        for j in range(n):
            m[i, j] = random.randint(1, 9)
        return m
print(matrix(4))