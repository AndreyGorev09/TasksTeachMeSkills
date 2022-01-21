a = ''
sum = 0
while True:
    a = input('Введите число или слово "stop", чтобы подсчитать сумму: ')
    if a == 'stop':
        break
    elif a.isdigit() == False:
        print('Ввели не число')
    elif int(a) % 5 == 0:
        continue
    else:
        sum+=int(a)
print(f'Сумма введенных чисел:{sum}')