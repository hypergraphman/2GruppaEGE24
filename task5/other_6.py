def n_to_p(n, p):
    r = []
    while n > 0:
        r = [n % p] + r
        n //= p
    return r


def f(n):
    s1 = n_to_p(n, 80)
    sum_odd = sum_even = 0
    for el in s1:
        if el % 2 == 0:
            sum_even += el
        else:
            sum_odd += el
    if sum_odd > sum_even:
        s1.append(n_to_p(sum_odd, 80)[-1])
    else:
        s1.append(n_to_p(sum_even, 80)[-1])
    # sum_odd = sum_even = 0
    # for el in s1:
    if s1[-1] % 2 == 0:
        sum_even += s1[-1]
    else:
        sum_odd += s1[-1]
    if sum_odd > sum_even:
        s1.append(n_to_p(sum_odd, 80)[-1])
    else:
        s1.append(n_to_p(sum_even, 80)[-1])
    res = 0
    for i in range(0, len(s1)):
        res += s1[i] * 80**(len(s1) - 1 - i)
    return res


for i in range(1, 1000):
    if f(i) > 1000000:
        print(i)
        break