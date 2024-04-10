def divs(n):
    s = {1, n}
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            s.add(i)
            s.add(n // i)
    return sorted(s)


def is_prime(n):
    if n < 1:
        return False
    return len(divs(n)) == 2


a = [int(x) for x in open('17.txt')]

# x = -10**6
# for el in a:
#     if abs(el) % 100 == 17 and el > x:
#         x = el
x = max(filter(lambda el: abs(el) % 100 == 17, a))

b = []
for p1, p2 in zip(a, a[1:]):
    if is_prime(p1) != is_prime(p2) and (p1 + p2) % x == 0:
        b.append(p1 * p2)
print(len(b), max(b))