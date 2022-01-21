def funcparitystr(str):
    x = str
    y = len(x)
    t = y%2
    if t == 0:
        return f'{x}! this line is even'
    else:
        return f'{x} this line is odd'