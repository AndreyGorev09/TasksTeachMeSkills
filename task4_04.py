a = ''
sum = 0
while True:
    a = input('Введите целое число или слово "stop" чтобы получить сумму кубов: ')
    if a == 'stop':
        break
    elif a.isdigit() == False:
        print('Ввели не число')
    else:
        sum+=pow(int(a),3)
print(f' Сумма кубов:{sum}')