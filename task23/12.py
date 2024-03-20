def f(c, e, h):
    if c >= e or h.count(0) > 7:
        return c == e
    return f(c + 1, e, h + [(c + 1) % 2]) + f(c * 2, e, h + [(c * 2) % 2]) + f(c * 3, e, h + [(c * 3) % 2])


print(f(1, 131, [1]))