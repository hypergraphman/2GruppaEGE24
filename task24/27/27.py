s = open('24.txt').readline().strip()
cur_len = 5
max_len = 0
for i in range(len(s) - 5):
    c = s[i: i + 6]
    if c[:3] != c[3:]:
        cur_len += 1
    else:
        cur_len = 5
    max_len = max(max_len, cur_len)
print(max_len)
