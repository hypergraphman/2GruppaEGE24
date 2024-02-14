f = open('24.txt')
s = f.readline().strip().replace('L', 'P').replace('N', 'P').replace('I', 'O').replace('A', 'O')
max_len = 0
temp = 'PO'
for j in range(0, len(temp)):
    cur_len = 0
    for i in range(j, len(s) - 1, 2):
        if s[i] + s[i + 1] == temp:
            cur_len += 1
        else:
            cur_len = 0
        max_len = max(max_len, cur_len)
print(max_len)