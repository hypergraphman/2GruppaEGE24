def f(n):
    d1, d2, d3 = map(int, str(n))
    return ''.join(map(str, sorted([d1 + d2, d2 + d3])[::-1]))


for n in range(100, 1000):
    if f(n) == '115':
        print(n)