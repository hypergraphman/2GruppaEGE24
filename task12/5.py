def divs(n):
    s = {1, n}
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            s.add(i)
            s.add(n // i)
    return sorted(s)


def is_prime(n):
    return len(divs(n)) == 2


for n in range(1, 100):
    if is_prime(103 + n * 7):
        print(n)
        break