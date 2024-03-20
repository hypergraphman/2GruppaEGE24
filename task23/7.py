def f(st, fn):
    if st < fn:
        return 0
    if st == fn:
        return 1
    moves = [f(st - 1, fn)]
    if st % 2 == 0:
        moves.append(f(st // 2, fn))
    if st % 3 == 0:
        moves.append(f(st // 3, fn))
    return sum(moves)


print(f(30, 1))