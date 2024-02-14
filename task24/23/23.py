f = open('24.txt')
s = f.readline().strip()
cur_len = 0
is_R = False
is_T = False
max_len = 0
for el in s:
    if el == 'R' and not is_R:
        is_R = True
        cur_len = 1
    elif el == 'R' and is_R and not is_T:
        cur_len += 1
    elif el == 'T' and not is_T:
        cur_len += 1
        is_T = True
    elif el == 'T' and is_T:
        cur_len += 1
    elif el == 'R' and is_T:
        cur_len = 1
        is_T = False
    else:
        cur_len = 0
        is_R = False
        is_T = False
    if cur_len > max_len and is_T and is_R:
        max_len = cur_len
print(max_len)