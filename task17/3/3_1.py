a = [int(x) for x in open('17.txt')]

avg = sum(a[1::2]) / len(a[1::2])

b = []
for t in zip(a, a[1:], a[2:]):
    t = sorted(t)
    if t[-1] % 2 == 0 and sum(el > avg for el in t) >= 2:
        b.append(t[-1] - t[0])
print(len(b), max(b))