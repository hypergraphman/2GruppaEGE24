from math import floor, ceil

f = open('26.txt')
# f = open('test.txt')
n = int(f.readline())
data = [int(x) for x in f]
data.sort()
x = n // 3
check = ceil(sum(data[:x]) * 0.67) + sum(data[x:])
naive = floor(sum(data[-x:]) * 0.67) + sum(data[:-x])
print(naive, check)