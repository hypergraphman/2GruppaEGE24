a = [int(x) for x in open('17.txt')]

s = 0
k = 0
for i in range(len(a)):
    if i % 2 != 0:
        s += a[i]
        k += 1
avg = s / k

b = []
for i in range(len(a) - 2):
    t1, t2, t3 = sorted([a[i], a[i + 1], a[i + 2]])
    if t3 % 2 == 0 and ((t1 > avg) + (t2 > avg) + (t3 > avg)) >= 2:
        b.append(t3 - t1)
print(len(b), max(b))