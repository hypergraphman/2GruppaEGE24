s = open('24.txt').readline().strip()
alp = '0123456789ABCDEF'
cur_len = 0
max_len = 0
for el in s:
    if el in alp:
        cur_len += 1
    else:
        cur_len = 0
    max_len = max(max_len, cur_len)
print(max_len)