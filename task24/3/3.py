f = open('24.txt')
s = f.readline().strip()
k = 0
for i in range(len(s) - 3):
    if len(set(s[i:i + 4])) == 4:
        k += 1
print(k)