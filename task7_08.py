def full_func(*args, **mean_type):
    if mean_type == 'arifmetic':
        return arifmetic_func(*args)
    else:
        return geometric_func(*args)
def arifmetic_func(*args):
    average = (sum(args)) / (len(args))
    return average
def geometric_func(*args):
    geo_mean = 1
    count = 0
    for i in args:
        geo_mean *= i
        count += 1
        return geo_mean ** (1/count)
a = full_func(2, 4, 6, 9, mean_type = 'arifmetic')
b = full_func(2, 4, 6, 9, mean_type = 'geometric')
print(f'Среднее арифмитическое равно: {a}')
print(f'Среднее геометрическое равно: {b}')