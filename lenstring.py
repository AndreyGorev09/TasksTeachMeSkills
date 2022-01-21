def funclenstr(string):
    y = len(string)
    if y > 5:
        return f'{y}'
    elif y < 5:
        return 'Need more!'
    elif y == 5:
        return 'It is five'