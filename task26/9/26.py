f = open('26.txt')
n, s = map(int, f.readline().split())
data = []
for i in range(n):
    cost, t = f.readline().split()
    cost = int(cost)
    data.append((cost, t))
data.sort()

k = 0
z = []
for cost, t in data:
    if s >= cost:
        s -= cost
        if t == 'Q':
            k += 1
        else:
            z.append(cost)
    elif t == 'Q' and s + z[-1] >= cost:
        s += z.pop()
        s -= cost
        k += 1
print(k, s)