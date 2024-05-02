f = open('26.txt')
n = int(f.readline())
a = [[0] * 501 for _ in range(501)]
for _ in range(n):
    row, cell = map(int, f.readline().split())
    a[row][cell] = 1
is_finish = False
for row in range(500, 0, - 1):
    for i in range(500, 6, -1):
        if a[row][i] + a[row][i - 6] == 2 and sum(a[row][i - 5:i]) == 0:
            print(row, i - 1)
            is_finish = True
            break
    if is_finish:
        break