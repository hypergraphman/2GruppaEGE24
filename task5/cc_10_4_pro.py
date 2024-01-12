def f(n):
    s1 = n // 3 if n % 3 == 0 else n - 1
    s2 = s1 // 5 if s1 % 5 == 0 else s1 - 1
    s3 = s2 // 7 if s2 % 7 == 0 else s2 - 1
    return s3


k = 0
for n in range(1, 10000):
    if f(n) == 1:
        k += 1
print(k)
