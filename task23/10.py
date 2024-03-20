def f(c, e, h):
    if c >= e:
        if 'BB' not in h:
            return c == e
        else:
            return 0
    return f(c + 1, e, h + 'A') + f(c * 2, e, h + 'B') + f(c * 3, e, h + 'C')


print(f(1, 15, ''))