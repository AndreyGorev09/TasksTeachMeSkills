def funcextent(a):
    try:
        if a.isdigit():
            return float(a)**2
        elif a.split("."):
            x = float(a)
        return x**2
    except:
        return "You didn't enter a number, use instead of a separator < . >"
