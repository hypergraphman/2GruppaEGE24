s = open('test.txt').readline().strip()
cur_len = 1
max_len = 1
for i in range(0, len(s) - 1):
    if s[i] + s[i + 1] not in ('BD', 'DB'):
        cur_len += 1
        max_len = max(max_len, cur_len)
    else:
        cur_len = 1
print(max_len)

