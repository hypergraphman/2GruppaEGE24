f = open('24.txt')
s = f.readline().strip().replace('T', 'G')
max_len = 0
for j in range(0, 2):
    cur_len = 0
    for i in range(j, len(s) - 1, 2):
        if s[i] + s[i + 1] == 'AG':
            cur_len += 1
        else:
            cur_len = 0
        max_len = max(max_len, cur_len)
print(max_len)