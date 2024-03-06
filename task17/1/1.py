a = [int(x) for x in open('17.txt')]

avg = sum(a) / len(a)

b = []
for p1, p2 in zip(a, a[1:]):
    if (p1 < avg or p2 < avg) and (p1 + p2) % 100 == 13:
        b.append(p1 + p2)

print(len(b), min(b))