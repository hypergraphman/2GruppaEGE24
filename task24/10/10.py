s = open('24.txt').readline().strip()
a = []
for i in range(1, len(s) - 1):
    if s[i - 1] < s[i] > s[i + 1]:
        a.append(i)
max_len = 0
for p1, p2, in zip(a, a[1:]):
    if p2 - p1 > max_len:
        max_len = p2 - p1
print(max_len)