def divs(n):
    s = {1, n}
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            s.add(i)
            s.add(n // i)
    return sorted(s)


def is_prime(n):
    return len(divs(n)) == 2


a = [int(x) for x in open('17.txt')]
mx = 0
for el in a:
    if el % 3 == 0 and el % 27 != 0 and el > mx:
        mx = el

b = []
for t in zip(a, a[1:], a[2:]):
    if (sum(is_prime(x) for x in t) == 2) != any(x > mx for x in t):
        b.append(sum(is_prime(x) for x in t))
print(len(b), sum(b))
