f = open('24.txt')
n, s = map(int, f.readline().split())
a = []
for i in range(n):
    t, cost, count = f.readline().split()
    cost, count = int(cost), int(count)
    if t == 'Z':
        s -= cost * count
    else:
        a.append((cost, count))
a.sort()
k = 0
last = 0
for i in range(len(a)):
    cost, count = a[i]
    if s >= cost * count:
        k += count
        s -= cost * count
    else:
        last = i
        break
cost, count = a[last]
print(k + s // cost, s % cost)