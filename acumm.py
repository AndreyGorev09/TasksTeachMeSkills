def funcaccum(string):
    try:
        sum = 0
        a = string.split(",")
        f = []
        for i in a:
            s = int(i)
            f.append(s)
        for j in f:
            sum += j
        return f'The sum of the entered numbers: {sum}'
    except:
        return "You didn't enter a list of numbers '1,2,3....n'"
