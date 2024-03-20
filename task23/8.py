def f(s, e):
    if s >= e or s == 7 or s == 12 or s == 17:
        return s == e
    return f(s + 1, e) + f(s + 4, e) + f(s * 3, e)


print(f(3, 15) * f(15, 30))