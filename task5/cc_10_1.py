def f(n):
    d1, d2, d3 = n // 100, n // 10 % 10, n % 10
    s1 = d1 + d2
    s2 = d2 + d3
    if s2 > s1:
        return str(s2) + str(s1)
    else:
        return str(s1) + str(s2)


for n in range(100, 1000):
    if f(n) == '115':
        print(n)