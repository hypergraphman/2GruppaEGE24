from string import ascii_lowercase, digits


def n_to_p(n, p):
    r = ''
    # alf = '0123456789abcdefghigklmnopqrstuvwxyz'
    alf = digits + ascii_lowercase
    while n > 0:
        r = alf[n % p] + r
        n //= p
    return r


t = n_to_p(5 * 49**5 + 3 * 7**8 - 7 * 7**4 + 100, 7)
print(sum(map(int, t)))
# s = 0
# for el in t:
#     s += int(el)
# print(s)