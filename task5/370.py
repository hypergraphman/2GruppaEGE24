from string import digits, ascii_uppercase


def n_to_p(n, p):
    alf = digits + ascii_uppercase
    r = ''
    while n:
        r = alf[n % p] + r
        n //= p
    return r


def f(n):
    s1 = n_to_p(n, 12)
    if n % 12 == 0:
        s2 = s1 + s1[-3:]
    else:
        s2 = n_to_p(n % 12 * 3, 12) + s1
    return int(s2, 12)


mx = 0
mx_n = 0
for i in range(1, 10000):
    if f(i) < 58000 and f(i) > mx:
        mx = f(i)
        mx_n = i
print(mx_n)