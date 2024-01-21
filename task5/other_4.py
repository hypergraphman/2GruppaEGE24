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
    s1 = n_to_p(n, 7)

    sum_digit = sum(map(int, s1))
    t = n_to_p(sum_digit, 7)
    s2 = '10' + s1[2:] + t
    sum_digit = sum(map(int, s2))
    t = n_to_p(sum_digit, 7)
    s3 = '100' + s2[3:] + t
    sum_digit = sum(map(int, s3))
    t = n_to_p(sum_digit, 7)
    s4 = '1000' + s3[4:] + t
    return int(s4, 7)


a = []
for i in range(11, 10000):
    if f(i) > 100000:
        a.append(f(i))
print(min(a))