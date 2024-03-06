a = [int(x) for x in open('17.txt')]

x = float('inf')
for el in a:
    if abs(el) % 10 == 7 and el < x:
        x = el

b = []
for p1, p2 in zip(a, a[1:]):
    if (p1 < x < p2 or p2 < x < p1) and abs(p1 + p2) % 4 == 0:
        b.append(p1 + p2)
print(len(b), max(b))
