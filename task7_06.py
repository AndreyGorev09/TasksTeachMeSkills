# Создать функцию, которая принимает на вход
# неопределенное количество аргументов и
# возвращает их сумму и максимальное из них.

x = [5, 7, 9, 4, 3, 2, 6, 4, 78, 6]
def args_sum_max(args):
    sum_args = sum(args)
    print(sum_args)
    max_arg = max(args)
    return max_arg


print(args_sum_max(x))