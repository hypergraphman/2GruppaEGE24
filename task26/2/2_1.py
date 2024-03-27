from collections import defaultdict

stuffs = defaultdict(list)
rating = defaultdict(list)

f = open('26.txt')
# f = open('test.txt')

p, n = map(int, f.readline().split())
for line in f:
    i, mark = map(int, line.split())
    stuffs[i].append(mark * 100)
print(stuffs)
for i in stuffs:
    stuffs[i].sort()
    x = int(len(stuffs[i]) * p / 100)
    if x > 0:
        stuffs[i] = stuffs[i][x:-x]
    rating[i].append(sum(stuffs[i]) // len(stuffs[i]))
    if len(stuffs[i]) % 2 == 0:
        med = sum(stuffs[i][len(stuffs[i]) // 2 - 1:len(stuffs[i]) // 2 + 1]) // 2
    else:
        med = stuffs[i][len(stuffs[i]) // 2]
    rating[i].append(abs(rating[i][0] - med))
print(rating)
mn = float('inf')
mx = 0
mx_i = 0
for i in rating:
    s, d = rating[i]
    if s < mn:
        mn = s
    if d >= mx:
        mx = d
        if i >= mx_i:
            mx_i = i
print(mn, mx_i)