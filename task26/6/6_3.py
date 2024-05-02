f = open('26.txt')
n = int(f.readline())
a = []
for _ in range(n):
    row, cell = map(int, f.readline().split())
    a.append((row, cell))
a.sort(reverse=True)
for p1, p2 in zip(a, a[1:]):
    row1, cell1 = p1
    row2, cell2 = p2
    if row1 == row2 and cell1 - cell2 - 1 == 5:
        print(row1, cell1 - 1)
        break