f = open('26.txt')
n = int(f.readline())
d = {}
for _ in range(n):
    row, place = map(int, f.readline().split())
    if row not in d:
        d[row] = []
    d[row].append(place)

f = False
for row in sorted(list(d.keys()), reverse=True):
    d[row].sort()
    for i in range(len(d[row]) - 1):
        p1, p2 = d[row][i], d[row][i + 1]
        if p2 - p1 == 3:
            print(row, d[row][i] + 1)
            f = True
            break
    if f:
        break