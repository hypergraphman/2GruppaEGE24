from math import ceil

f = open('26.txt')
# f = open('test.txt')
f.readline()
data = [int(x) for x in f]
# print(data)
s = 0
stuffs_more_500 = []
for el in data:
    if el > 500:
        stuffs_more_500.append(el)
    else:
        s += el
stuffs_more_500.sort()
n = len(stuffs_more_500) // 2
s += ceil(sum(stuffs_more_500[:n]) * 0.8) + sum(stuffs_more_500[n:])
print(s, stuffs_more_500[n - 1])