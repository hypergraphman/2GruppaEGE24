a = [0] * 20
a[19] = 1
for i in range(18, 2 - 1, -1):
    if i != 5 and i != 15:
        a[i] += a[i + 1]
        if i + 4 <= 19:
            a[i] += a[i + 4]
        if i * 2 <= 19:
            a[i] += a[i * 2]
        if i * 2 + 1 <= 19:
            a[i] += a[i * 2 + 1]
print(a[2])