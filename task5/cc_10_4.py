def f(n):
    if n % 3 == 0:
        s1 = n // 3
    else:
        s1 = n - 1
    if s1 % 5 == 0:
        s2 = s1 // 5
    else:
        s2 = s1 - 1
    if s2 % 7 == 0:
        s3 = s2 // 7
    else:
        s3 = s2 - 1
    return s3


k = 0
for n in range(1, 10000):
    if f(n) == 1:
        k += 1
print(k)
