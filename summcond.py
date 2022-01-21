def funcsummcond(g):
    sum = 0
    a = g.split(",")
    f = []
    for i in a:
        s = int(i)
        f.append(s)
    for j in f:
        if j>=10:
            sum+=j
    return sum