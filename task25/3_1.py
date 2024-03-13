from itertools import product

digits = []
for i in range(6 + 1):
    digits += [''.join(x) for x in product('0123456789', repeat=i)]

for d1 in digits:

    digits2 = []
    for i in range(6 - len(d1) + 1):
        digits2 += [''.join(x) for x in product('0123456789', repeat=i)]

    for d2 in digits2:
        t = f'9{d1}4{d2}0'
        a = []
        for p1, p2 in zip(t, t[1:]):
            a.append(p1 > p2)
        if all(a) and int(t) % 47 == 0:
            print(t, int(t) // 47)
