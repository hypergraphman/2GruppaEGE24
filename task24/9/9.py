f = open('24.txt')
s = f.readline().strip()
cur_len = 1
max_len = 1
max_i = 0
for i in range(1, len(s)):
    if s[i - 1] < s[i]:
        cur_len += 1
    else:
        cur_len = 1
    if cur_len > max_len:
        max_len = cur_len
        max_i = i
print(s[max_i - max_len + 1: max_i + 1])