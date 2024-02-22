from functools import lru_cache


@lru_cache(None)
def f(n):
    if n > 2024:
        return n
    if n <= 2024:
        return n * f(n + 1)


for i in range(2024, 0, -1):
    f(i)

print(f(2) // f(2024))