f = open('24.txt')
s = f.readline().strip()
max_len = cur_len = 1
for c1, c2 in zip(s, s[1:]):
    if c1.isdigit() == c2.isalpha():
        cur_len += 1
    else:
        cur_len = 1
    max_len = max(max_len, cur_len)
print(max_len)
