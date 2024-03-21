def f(c, e, k):
    if c > e or k > 6:
        return 0
    if c == e:
        return 1
    m = [f(c + 1, e, k + 1),
         f(c * 2, e, k + 1),
         f(c ** 2, e, k + 1)]
    return sum(m)


count = 0
for i in range(-1000, 131):
    if f(i, 131, 0) > 0:
        count += 1
print(count)