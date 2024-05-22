from string import digits, ascii_uppercase


def n_to_p(n, p):
    alf = digits + ascii_uppercase
    r = ''
    while n:
        r = alf[n % p] + r
        n //= p
    return r


def f(n):
    s1 = n_to_p(n, 3)
    if n % 2 == 0:
        s2 = '2' + s1 + n_to_p(int(s1[-1], 3) * 2, 3)
    else:
        s2 = n_to_p(int(s1[0], 3) * 2, 3) + s1 + '2'
    return int(s2, 3)


s = set()
for i in range(1, 100):
    if f(i) > 100:
        s.add(f(i))
print(min(s))