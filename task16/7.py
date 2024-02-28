from functools import lru_cache


@lru_cache(None)
def f(n):
    if n < 10:
        return n
    if n % 3 == 0:
        return f(n - 1) + 3 * n * n
    return f(n - 1) + n**3


k = 0
for i in range(1, 32000):
    if f(i) < 10**9:
        k += 1
print(k)

