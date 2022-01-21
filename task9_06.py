from datetime import datetime
time = datetime.now()

def decorator_func(func):
    def time_func():
        t0 = datetime.now()
        print(func())
        t1 = datetime.now()
        delta = t1 - t0
        s = delta.total_seconds()
        print(f'{func.__name__} отработала за {s} секунд.')
    return time_func()
@decorator_func
def gener_list():
    list_gen_digit = []
    for n in range(10000):
        list_gen_digit.append(n)
    return list_gen_digit