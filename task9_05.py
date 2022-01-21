from functools import reduce
list_digits = [2, 3, 4, 5, 6, 7, 8, 9]
func_d = reduce(lambda a, x: a*x, filter(lambda x: x%3==0, list_digits))
print(func_d)