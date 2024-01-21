from string import ascii_lowercase, digits


def n_to_p(n, p):
    r = ''
    # alf = '0123456789abcdefghigklmnopqrstuvwxyz'
    alf = digits + ascii_lowercase
    while n > 0:
        r = alf[n % p] + r
        n //= p
    return r


def f(n):
    s1 = n_to_p(n, 4)
    if n % 2 != 0:
        s2 = '2' + s1 + '11'
    else:
        s2 = '13' + s1 + '02'
    return int(s2, 4)


a = []
for i in range(1, 100):
    if f(i) > 1000:
        a.append(f(i))
print(min(a))

for i in range(1, 100):
    print(i, f(i))