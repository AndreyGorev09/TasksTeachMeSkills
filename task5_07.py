import random
a = int(input(f'Введите число от: '))
b = int(input(f'Введите число до: '))
c = int(input(f'Введите количество попыток: '))
d = int(input(f'Введите Ваше число: '))
x = random.randint(a, b)
c -= 1
while True:
    if x == d:
        c -= 1
        print('Вы молодчик, так держать!!!')
        break
    elif x > d:
        c -= 1
        print('Неизвестное число больше, попробуйте еще раз!')
        d = int(input(f'{""}'))
        if c <= 0:
            print(f'Не Ваш день, попробуйте сыграть еще раз, правильный ответ {x}!')
            break
    elif x < d:
        c -= 1
        print('Неизвестное число меньше, попробуйте еще раз!')
        d = int(input(f'{""}'))
        if c <= 0:
            print(f'Не Ваш день, попробуйте сыграть еще раз, правильный ответ {x}!')
            break