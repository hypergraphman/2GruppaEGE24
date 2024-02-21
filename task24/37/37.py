s = open('24.txt').readline().strip()
a = [i for i in range(1, len(s) - 1) if s[i - 1] + s[i] + s[i + 1] == '131']
mx = 0
for i in range(len(a) - 132):
    if a[i + 132] - a[i] - 1 > mx:
        mx = a[i + 132] - a[i] + 1
print(mx)