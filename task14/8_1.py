from string import ascii_lowercase, digits
from collections import Counter


def n_to_p(n, p):
    r = ''
    # alf = '0123456789abcdefghigklmnopqrstuvwxyz'
    alf = digits + ascii_lowercase
    while n > 0:
        r = alf[n % p] + r
        n //= p
    return r


t = n_to_p(45*400**10 - 8**5*5**8 + 16*20**3 - 33, 20)
print(Counter(t))
k = 0
for el in t:
    if el.isdigit():
        k += 1
print(k)