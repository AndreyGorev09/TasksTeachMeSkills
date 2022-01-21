list_a = (3, 6, 9, -2, 6, -9, -2, 4, 12, -122, -34, 56, 999, 23, -66)
def sum_a(*n):
    while True:
        value_even_a = 0
        value_uneven_a = 0
        for a in list(*n):
            if a > 0:
                value_even_a+=a
                list_value_even_a = []
                list_value_even_a.append(value_even_a)
            else:
                value_uneven_a+=a
                list_value_uneven_a = []
                list_value_uneven_a.append(a)
        return (f'Сумма положительных чисел: {value_even_a}, сумма отрицательных чисел: {value_uneven_a}')
print(sum_a(list_a))