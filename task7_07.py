# Создать функцию, которая принимает на вход
# неопределенное количество именных
# аргументов и выводит на экран те из них,
# длина ключа которых четна.

def full_func(**kwargs):
    for x in kwargs:
        if kwargs.get(x) % 2 == 0:
            print(x)
print(full_func(a=4,b=5,c=6))