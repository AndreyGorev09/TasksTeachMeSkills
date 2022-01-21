a = int(input('Введите число от: '))
b = int(input('Введите число до: '))
a+=1
b+=1
for i in range(a):
    c = (pow(i, 3))
for i in range(b):
    d = (pow(i, 3))
    e = [c, d]
    f = sum(e)
print(f)