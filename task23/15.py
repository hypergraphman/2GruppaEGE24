def f(s, k):
    global a
    if k == 4:
        return s
    a.append(f(s + 3, k + 1))
    a.append(f(s + 1, k + 1))
    a.append(f(s * 3, k + 1))

a = []
f(1, 0)
print(len(set(a) - {None}))