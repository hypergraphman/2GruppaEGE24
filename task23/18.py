def f(st, fn, h):
    if h > 7:
        return 0
    if st == fn and h == 7:
        return 1
    m = [f(st - 5, fn, h + 1),
         f(st * (-2), fn, h + 1)]
    return sum(m)


count = 0
for a in range(1, 10000):
    if f(131, a, 0) > 0:
        count += 1
print(count)