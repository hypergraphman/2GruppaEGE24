with open('26.txt') as f:
    n_cells = int(f.readline())
    a = [0] * (n_cells + 1)
    n_mans = int(f.readline())
    p = []
    for _ in range(n_mans):
        s, e = map(int, f.readline().split())
        p.append((s, e))
p.sort()
k = 0
last = 0
for s, e in p:
    for i in range(1, n_cells + 1):
        if s > a[i]:
            a[i] = e
            k += 1
            last = i
            break
print(k, last)
