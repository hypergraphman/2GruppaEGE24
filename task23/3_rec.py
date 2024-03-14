def f(st, fin):
    if st == 15 or st == 5 or st < fin:
        return 0
    if st == fin:
        return 1
    moves = [
        f(st - 1, fin),
        f(st - 4, fin),
        f(st // 2, fin)
    ]
    return sum(moves)


print(f(19, 2))