a = [0] * 1000
a[1] = 1
for i in range(2, 9 + 1):
    if i - 2 > 0:
        a[i] += a[i - 2]
    if i - 3 > 0:
        a[i] += a[i - 3]
    if i % 2 == 0:
        a[i] += a[i // 2]
print(a[9])
for i in range(10, 20 + 1):
    if i - 2 >= 9:
        a[i] += a[i - 2]
    if i - 3 >= 9:
        a[i] += a[i - 3]
    if i % 2 == 0 and i // 2 >= 9:
        a[i] += a[i // 2]
print(a[20])