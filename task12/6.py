k = 0
for n in range(1, 1000):
    s = '0' + '2' * n
    while '02' in ...
        ...
    if sum(map(int, s)) == 100:
        k += 1
print(k)