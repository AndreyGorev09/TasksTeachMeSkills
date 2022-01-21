a = int(input('Введите число "А": '))
b = int(input('Введите число "В": '))
b += 1
while True:
    if a < b:
        for i in range(a, b):
            print(i)
            c = b-a
        print(f'Всего количество чисел от А до В:{c}')
        break
    elif a >= b:
	    print('Число "А" должно быть меньше числа "В"')
	    break
