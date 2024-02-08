f = open('24.txt')
s = f.readline().strip()
a = [0] * 128
for i in range(len(s) - 1):
    if s[i] == 'V':
        a[ord(s[i + 1])] += 1
mx = 0
mx_i = 0
for i in range(ord('A'), ord('Z') + 1):
    if a[i] > mx:
        mx = a[i]
        mx_i = i
print(chr(mx_i) + str(mx))
