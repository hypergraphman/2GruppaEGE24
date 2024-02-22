# 1 1 2 3 5 8 13 21 34 55
# n = int(input())
# f_pre = 1
# f_cur = 1
# for i in range(3, n + 1):
#     f_cur, f_pre = f_cur + f_pre, f_cur
# print(f_cur)
from time import time
from functools import lru_cache


@lru_cache(None)
def f(n):
    if n in (1, 2):
        return 1
    if n > 2:
        return f(n - 1) + f(n - 2)


n = int(input())
for i in range(1, n + 1):
    t = time()
    print(i, f(i), time() - t)