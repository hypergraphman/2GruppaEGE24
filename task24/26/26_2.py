lines = open('26.txt').readline().strip().split('Z')[:-1]
min_c = float('inf')
for line in lines:
    i = line.find('A')
    if i not in (-1, len(line) - 1) and len(line) - i + 1 < min_c:
        min_c = len(line) - i + 1
print(min_c)
