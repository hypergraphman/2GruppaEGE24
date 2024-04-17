*a, = map(int, open('17.txt'))
mn = 10000
for el in a:
    if 100 <= el < 1000 and el % 100 == 11 and el < mn:
        mn = el

b = []
for i in range(len(a) - 1):
    p1, p2 = a[i], a[i + 1]
    if ((100 <= p1 < 1000 and not (100 <= p2 < 1000) or
       not (100 <= p1 < 1000) and 100 <= p2 < 1000) and
       (p1 - p2) % mn == 0):
        b.append(p1 + p2)
print(len(b), max(b))
