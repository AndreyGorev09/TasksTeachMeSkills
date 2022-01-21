def funcrub(rub):
    r = int(rub)%10
    if r == 1:
        return f'{rub} ruble'
    elif 2 <= r <= 4:
        return f'{rub} rubles'
    else:
        return f'{rub} rubles'
def funccoin(coin):
    c = int(coin) % 10
    if int(c) == 1:
        return f'{coin} coin'
    elif 2 <= c <= 4:
        return f'{coin} coins'
    else:
        return f'{coin} coins'
