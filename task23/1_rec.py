from functools import lru_cache


@lru_cache(None)
def f(st, fin):
    if st == fin:
        return 1
    if st > fin:
        return 0
    moves = [f(st + 1, fin),
             f(st * 2, fin),
             f(st * 3, fin)]
    return sum(moves)


for i in range(500, 1, -1):
    f(i, 500)

print(f(1, 500))
