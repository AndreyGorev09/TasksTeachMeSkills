list_lot_digit = []
dict_value_lot = {}
list_digit = [12, 34, 56, 65, 3, 45, 4, 7, 4, 23, 4, 778, 23, 4, 12, 78, 7]
for i in list_digit:
    list_lot_digit.append(list_digit.count(i))
    dict_value_lot.update(zip(list_digit, list_lot_digit))
print(dict_value_lot)