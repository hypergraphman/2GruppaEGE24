def divs(n):
    s = {n}
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            if i % 2 == 0:
                s.add(i)
            if n // i % 2 == 0:
                s.add(n // i)
    return sorted(s)


for i in range(100_000_000, 101_000_000 + 1):
    t = divs(i)
    if len(t) == 3:
        print(i, t[1])
