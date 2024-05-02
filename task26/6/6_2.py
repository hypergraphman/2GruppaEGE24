f = open('26.txt')
n = int(f.readline())
a = dict()
for _ in range(n):
    row, cell = map(int, f.readline().split())
    a[row] = a.setdefault(row, []) + [cell]
is_finish = False
for row in sorted(a.keys(), reverse=True):
    a[row].sort(reverse=True)
    for p1, p2 in zip(a[row], a[row][1:]):
        if p1 - p2 - 1 == 5:
            print(row, p1 - 1)
            is_finish = True
            break
    if is_finish:
        break
