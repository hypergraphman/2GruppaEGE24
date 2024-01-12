for n in range(100, 1000):
    d1, d2, d3 = n // 100, n // 10 % 10, n % 10
    s1 = d1 + d2
    s2 = d2 + d3
    r = ''
    if s1 > s2:
        r = str(s1) + str(s2)
    else:
        r = str(s2) + str(s1)
    if r == '115':
        print(n)
