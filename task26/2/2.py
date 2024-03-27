# f = open('test.txt')
f = open('26.txt')
stuffs = [[] for _ in range(10001)]
rating = [[] for _ in range(10001)]
p, n = map(int, f.readline().split())
for line in f:
    i, mark = map(int, line.split())
    stuffs[i].append(mark)
# print(stuffs)
for i in range(len(stuffs)):
    if stuffs[i]:
        stuffs[i].sort()
        x = int(len(stuffs[i]) * p / 100)
        if x > 0:
            stuffs[i] = stuffs[i][x:-x]
        for j in range(len(stuffs[i])):
            stuffs[i][j] *= 100
        rating[i].append(sum(stuffs[i]) // len(stuffs[i]))
        if len(stuffs[i]) % 2 == 0:
            rating[i].append(sum(stuffs[i][len(stuffs[i]) // 2 - 1:len(stuffs[i]) // 2 + 1]) // 2)
        else:
            rating[i].append(stuffs[i][len(stuffs[i]) // 2])
# print(rating[1:4])
mn = float('inf')
mx = 0
mx_i = 0
for i in range(len(rating)):
    if rating[i]:
        s, m = rating[i]
        if s < mn:
            mn = s
        if abs(m - s) >= mx:
            mx = abs(m - s)
            mx_i = i
print(mn, mx_i)
