a = [int(x) for x in open('17.txt')]

mx = 0
for el in a:
    if el % 1000 == 131 and el > mx:
        mx = el

b = []
for i in range(len(a) - 2):
    t1, t2, t3 = sorted([a[i], a[i + 1], a[i + 2]])
    if ((1000 <= t1 < 10000) + (1000 <= t2 < 10000) + (1000 <= t3 < 10000)) == 1 and t1 + t2 < mx:
        b.append(min(t2 - t1, t3 - t2))
print(len(b), min(b))