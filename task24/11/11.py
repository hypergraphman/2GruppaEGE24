f = open('24.txt')
s = f.readline().strip() + chr(ord('0') - 1)
cur_len = 1
k = 0
for i in range(1, len(s)):
    if s[i - 1] <= s[i]:
        cur_len += 1
    else:
        if cur_len == 6:
            k += 1
        cur_len = 1
print(k)