def quadratic_equation(a:int,b:int,c:int):
    while True:
        D = b ** 2 - 4 * a * c
        x1 = (-b + D**0.5) / 2 * a
        x2 = (-b - D**0.5) / 2 * a
        if D > 0:
            print(f'Значение корня "x1" равняется:{x1}')
            print(f'Значение корня "x2" равняется:{x2}')
            break
        elif D == 0:
            print(f'Значение корней "x1" и "x2" одинаковое и равняется:{x1}')
            break
        else:
            print('Корней на множестве действительных чисел нет!\n')
            break
print(quadratic_equation(5,7,2))