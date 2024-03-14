def f(st, fn):
    if st > fn:
        return 0
    if st == fn:
        return 1
    moves = [
        f(st + 2, fn),
        f(st + 3, fn),
        f(st * 2, fn)
    ]
    return sum(moves)


print(f(1, 9) * f(9, 20))