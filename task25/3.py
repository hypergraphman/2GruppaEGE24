from fnmatch import fnmatch

for i in range(47, 10**10, 47):
    t = str(i)
    a = []
    for p1, p2 in zip(t, t[1:]):
        a.append(p1 > p2)
    if all(a) and fnmatch(t, '9*4*0'):
        print(i, i // 47)
