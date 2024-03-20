def f(s, e, h):
    if s > e:
        return 0
    if s == e:
        if h[-2] in '23':
            return 1
        else:
            return 0
    m = [f(s + 1, e, h + '1'),
         f(s * 2, e, h + '2'),
         f(s * 3, e, h + '3')]
    return sum(m)


print(f(1, 28, ''))