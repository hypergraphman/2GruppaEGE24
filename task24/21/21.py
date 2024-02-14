f = open('24.txt')
s = f.readline().strip()
temp = 'LISA'
max_len = 0
for _ in range(0, len(temp)):
    temp = temp[1:] + temp[0]
    cur_len = 0
    for el in s:
        if temp[cur_len % len(temp)] == el:
            cur_len += 1
        elif el == temp[0]:
            cur_len = 1
        else:
            cur_len = 0
        max_len = max(max_len, cur_len)
print(max_len)