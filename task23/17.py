from functools import lru_cache


@lru_cache(None)
def f(c, e):
    if c > e or c == 11:
        return 0
    if c == e:
        return 1
    m = [f(c + 1, e),
         f(c + 3, e),
         f(c * 3, e)]
    return sum(m)


for i in range(12, 400):
    if f(1, 10) * f(10, i) == 132:
        print(i)