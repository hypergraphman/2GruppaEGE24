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
    s1 = n_to_p(n, 3)
    if n % 3 == 0:
        s2 = '1' + s1 + '01'
    else:
        s2 = s1 + n_to_p(n % 3 * 4, 3)
    return int(s2, 3)


# print(f(13))

a = []
for i in range(1, 140):
    if f(i) < 1199:
        a.append(i)
print(max(a))

for i in range(97, 140):
    print(i, f(i))