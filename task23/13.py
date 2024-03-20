def f(s, e, k):
    if s >= e or k == 7:
        return s == e
    return f(s + 2, e, k + 1) + f(s + 3, e, k + 1) + f(s * 2, e, k + 1)


print(f(1, 130, 0))