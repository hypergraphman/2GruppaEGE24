a = [int(x) for x in open('17.txt')]

s = 0
k = 0
for el in a:
    if abs(el) % 100 == 19:
        s += el
        k += 1
avg = s / k

b = []
for q in zip(a, a[1:], a[2:], a[3:]):
    if any(abs(x) % 15 == 12 for x in q) and sum(x < avg for x in q) >= 2:
        b.append(sum(q))
print(len(b), max(b))