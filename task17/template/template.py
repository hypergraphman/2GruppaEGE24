a = [int(x) for x in open('17.txt')]

x = 0
for el in a:
    if True:
        x += 1

b = []
# for i in range(len(a) - 1):
#     p1, p2 = a[i], a[i + 1]
for p1, p2 in zip(a, a[1:]):
    if p1 == p2:
        b.append(p1 + p2)
print(len(b), max(b))