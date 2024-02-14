f = open('24.txt')
s = f.readline()
cur_len = 1
max_len = 1
for c1, c2 in zip(s, s[1:]):
    if not ({c1, c2} <= {'K', 'E', 'G'}):
        cur_len += 1
    else:
        cur_len = 1
    max_len = max(max_len, cur_len)
print(max_len)