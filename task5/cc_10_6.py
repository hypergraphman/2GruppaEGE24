def f(n):
    a = []
    s = str(n)
    for p1, p2 in zip(s, s[1:]):
        a.append(int(p1 + p2))
    return max(a) + min(a)


for i in range(11, 1000):
    if f(i) == 131:
        print(i)
        break