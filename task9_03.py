volue_digit = [3, 5, 6, 12, 89]
new_list_volue_digit = []

def volue_d(n):
    for i in list(n):
        new_list_volue_digit.append(str(i))
    return new_list_volue_digit
print(volue_d(volue_digit))

list_digit = [2,4]
func_d = list(map(lambda digit: f'{digit}', list_digit))
print(func_d)