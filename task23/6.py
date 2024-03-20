def f(s, e):
    if s >= e:
        return s == e
    return f(s + 1, e) + f(s * 3, e) + f((s // 10 + 1) * 10, e)


print(f(1, 10) * f(10, 20) * f(20, 60))