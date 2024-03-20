def f(s, e, k):
    global ch
    if s >= e or k == ch:
        return s == e
    return f(s + 2, e, k + 1) + f(s + 3, e, k + 1) + f(s * 2, e, k + 1)


for ch in range(1, 10):
    if f(1, 130, 0) > 0:
        print(ch)