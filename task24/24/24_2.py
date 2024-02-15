f = open('24.txt')
s = f.readline().strip()
max_len = 0
for j in range(0, 3):
    cur_len = 0
    for i in range(j, len(s) - 2, 3):
        if s[i] == '1' and s[i + 2] == '1' or s[i] == '3' and s[i + 2] == '3':
            cur_len += 1
        else:
            cur_len = 0
        max_len = max(max_len, cur_len)
print(max_len)