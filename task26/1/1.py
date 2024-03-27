f = open('26.txt')
s, n = map(int, f.readline().split())
a = sorted([int(x) for x in f.readlines()])
i = 0
while s - a[i] >= 0:
    s -= a[i]
    i += 1
print(i)
s += a[i - 1]
mx = 0
for el in a:
    if el > mx and el <= s:
        mx = el
print(mx)