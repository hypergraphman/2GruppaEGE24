a = [int(x) for x in open('17.txt')]

big3, big2, big1 = sorted(a)[-3:]

b = []
for q in zip(a, a[1:], a[2:], a[3:]):
    q4, q3, q2, q1 = sorted(q)
    if q3 + q2 + q1 > big1 + big2 and q4 < big3 / 2:
        b.append(sum(q))
print(len(b), min(b))
