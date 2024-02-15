s = open('26.txt').readline().strip()
c = 0
min_c = float('inf')
is_a = False
for i in range(len(s)):
    if is_a:
        c += 1
    if i + 1 < len(s) and s[i] == 'A' and s[i + 1] != 'Z':
        c = 1
        is_a = True
    if is_a and s[i] == 'Z':
        min_c = min(min_c, c)
        is_a = False
        c = 0
print(min_c)
