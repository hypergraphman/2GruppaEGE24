f = open('24.txt')
s = f.readline().strip()
templates = ['1' + x + '1' for x in '0123456789'] + ['3' + x + '3' for x in '0123456789']
max_len = 0
for j in range(0, 3):
    cur_len = 0
    for i in range(j, len(s) - 2, 3):
        if s[i] + s[i + 1] + s[i + 2] in templates:
            cur_len += 1
        else:
            cur_len = 0
        max_len = max(max_len, cur_len)
print(max_len)