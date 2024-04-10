def check(n):
    return 100 <= n < 1000 and 3 == len(set(str(n)))


a = [int(x) for x in open('17.txt')]

# mn = 10**6
# for el in a:
#     if check(el) and el < mn:
#         mn = el
mn = min(el for el in a if check(el))

b = []
for i in range(len(a) // 2):
    p1, p2 = a[i], a[-1 - i]
    if p1 * p2 % mn == 0:
        b.append(p1 + p2)
print(len(b), min(b))
