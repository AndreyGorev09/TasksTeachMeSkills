import math
def x(numer: int, denomen: int):
    calculetion = (math.sqrt(numer) + numer) / denomen
    return calculetion
sum_x = x(5, 2) + x(12, 2) + x(19, 2)
print(sum_x)