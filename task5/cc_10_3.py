def f(n):
    d1, d2, d3 = n // 100, n // 10 % 10, n % 10
    a = [d1 * 10 + d2, d1 * 10 + d3,
         d2 * 10 + d1, d2 * 10 + d3,
         d3 * 10 + d1, d3 * 10 + d2]
    # print(a)
    b = []
    for x in a:
        if x > 9:
            b.append(x)
    # print(b)
    return max(b) - min(b)


for n in range(100, 1000):
    if f(n) == 80:
        print(n)