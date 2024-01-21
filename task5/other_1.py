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
    s2 = s1 + str(n % 3)
    s3 = s2 + str(n % 3)
    s4 = s3 + str(n % 3)
    return int(s4, 3)


a = []
for i in range(1, 10000):
    if 1000 <= f(i) < 10000:
        a.append(f(i))
print(min(a))


for i in range(1, 10000):
    if f(i) <= min(a):
        print(i, f(i))