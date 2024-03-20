def f(c, e, h):
    if c >= e:
        if h.count('B') <= 2:
            return c == e
        else:
            return 0
    return f(c + 1, e, h + 'A') + f(c + 2, e, h + 'B') + f(c * 3, e, h + 'C')


print(f(1, 13, ''))