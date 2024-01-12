for n in range(10000, 100000):
    d1, d2, d3, d4, d5 = n // 10000, n // 1000 % 10, n // 100 % 10, n // 10 % 10, n % 10
    # d1, d2, d3, d4, d5 = map(int, str(n))
    s1 = d1 + d3 + d5
    s2 = d2 + d4
    r = ''
    if s1 > s2:
        r = str(s2) + str(s1)
    else:
        r = str(s1) + str(s2)

    # if n == 13885:
    #     print(r)
    if r == '321':
        print(n)