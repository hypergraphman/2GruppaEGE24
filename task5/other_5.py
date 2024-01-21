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
    s1 = n_to_p(n, 20)
    s2 = ''
    for el in s1:
        if el == '9':
            s2 += 'a'
        elif el == 'j':
            s2 += 'j'
        else:
            s2 += chr(ord(el) + 1)
    return int(s2, 20)


a = set()
for i in range(1, 100000):
    if 1000 <= f(i) <= 10000:
        a.add(f(i))
print(len(a))

a = []
for i in range(1, 100000):
    if 1000 <= f(i) <= 10000 and f(i) not in a:
        a.append(f(i))
print(len(a))