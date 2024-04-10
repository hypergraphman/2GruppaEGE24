a = [int(x) for x in open('17.txt')]

x = -100
for el in a:
    if -100 < el < 100 and not (-10 < x < 10) and el > x:
        x = el

A = -float('inf')
for q in zip(a, a[1:], a[2:], a[3:]):
    find = abs(q[0]) % 10
    if all(abs(eq) % 10 == find for eq in q) and sum(q) > A:
        A = sum(q)
# A = -10**9
# for i in range(len(a) - 3):
#     q = [a[i], a[i + 1], a[i + 2], a[i + 3]]
#     find = abs(q[0]) % 10
#     is_find = True
#     for eq in q:
#         if abs(eq) % 10 != find:
#             is_find = False
#     if is_find:
#         sm = sum(q)
#         if sm > A:
#             A = sm

b = []
for five in zip(a, a[1:], a[2:], a[3:], a[4:]):
    if sum(ef < A for ef in five) == 1 and sum(five) % x == 0:
        b.append(sum(five))
print(len(b), min(b))