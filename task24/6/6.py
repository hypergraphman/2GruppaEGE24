f = open('24.txt')
s = f.readline().strip()
cur_len = 1
max_len = 1
max_i = None
for i in range(len(s) - 1):
    c1, c2 = s[i], s[i + 1]
    if c1 != c2:
        cur_len += 1
    else:
        cur_len = 1
    if cur_len >= max_len:
        max_len = cur_len
        max_i = i + 1
print(s[max_i - max_len + 1:max_i + 1])

# XYZYXZYZXYZXYZYXYXYXZYZXYXYZXYX
# XYZYXZYZXYZXYZYXYXYXZYZXYXYZXYX