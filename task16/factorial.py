# n! = 1 * 2 * 3 * ... * (n - 1) * n

# n = int(input())
# f = 1
# for i in range(1, n + 1):
#     f *= i
# print(f)
from functools import lru_cache


@lru_cache(None)
def f(n):
    if n in (0, 1):
        return 1
    if n > 1:
        return n * f(n - 1)


n = int(input())

for i in range(1, n):
    f(i)

print(f(n))