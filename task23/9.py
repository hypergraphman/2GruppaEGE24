def f(c, e):
    if c >= e:
        return c == e
    return f(c + 1, e) + f(c * 2, e) + f(c * 2 + 1, e)


print(f(2, 16))