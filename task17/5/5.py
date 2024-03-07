a = [int(x) for x in open('17.txt')]

b = []
for t in zip(a, a[1:], a[2:]):
    t1, t2, t3 = sorted(t)
    if (t2 - t1 == t3 - t2 > 0
       and t1 % 10 != t2 % 10 != t3 % 10 != t1 % 10):
       b.append(t2 - t1)
print(len(b), min(b))