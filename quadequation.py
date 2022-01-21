def funcquad(a:float, b:float, c:float):
    D = b**2 - 4*a*c
    if D > 0:
        x_1 = -(b + D**0.5) / (2*a)
        x_2 = -(b - D**0.5) / (2*a)
        return f'First root: {x_1}, Second root: {x_2}'
    elif D == 0:
        x_1 = -(b + D**0.5) / (2*a)
        return f'First root: {x_1}'
    else:
        return 'There are no valid roots'
