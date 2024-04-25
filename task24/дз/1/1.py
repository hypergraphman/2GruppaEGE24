s = open('24.txt').read().strip()
k = 0
for t1, t2, t3 in zip(s, s[1:], s[2:]):
    if t1 in 'ABC' and t2 in 'CDE' and t3 in 'BCDF' and len({t1, t2, t3}) == 3:
        k += 1
print(k)