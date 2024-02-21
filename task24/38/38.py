lines = [line.strip() for line in open('24.txt')]
k = 0
for line in lines:
    f = 0
    for i in range(len(line) - 3):
        if line[i] + line[i + 3] == 'KE':
            f = 1
    k += f
print(k)