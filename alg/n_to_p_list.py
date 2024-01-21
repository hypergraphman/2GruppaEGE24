def n_to_p(n, p):
    r = []
    while n > 0:
        r = [n % p] + r
        n //= p
    return r


print(n_to_p(194, 5))
print(n_to_p(255, 16))