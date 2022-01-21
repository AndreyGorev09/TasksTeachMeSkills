list_value = (2, 4, 6, 0, 2, 8, 0, 1, 0, 3)

def is_power_n(n, *k):
    while True:
        volue_k = 0
        for k in list(*k):
            if n > 1 and k > 0:
                volue_k+=1
                print(True)
            else:
                print(False)
        break
    return (f'Количество степеней числа "N": {volue_k}')
print(is_power_n(2, list_value))