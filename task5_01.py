import random
m = []
n = 3
for i in range(n):
    m.append([])
    for j in range(n):
       x = m[i].append(random.randint(0, 9))
print(m)