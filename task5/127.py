def f(n):
    a1, a2, a3, a4 = map(int, str(n))
    a = [a1 + a2, a2 + a3, a3 + a4]
    del a[a.index(max(a))]
    a.sort()
    return str(a[0]) + str(a[1])


for i in range(1000, 10000):
    if f(i) == '1114':
        print(i)