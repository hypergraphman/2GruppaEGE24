def f(s, k):
    global a
    if k == 7:
        if s > 0:
            return s
        return None
    a.add(f(s - 5, k + 1))
    a.add(f(s * (-2), k + 1))


a = set()
f(131, 0)
print(len(a - {None}))