from collections import Counter

s = open('24.txt').readline().strip()
a = []
for i in range(0, len(s) - 4):
    c1, c2, c3, c4, c5 = s[i], s[i + 1], s[i + 2], s[i + 3], s[i + 4]
    if c1 == '1' and c2 == '3' and c4 == '3' and c5 == '1' and c3 not in ('0', '3', '5', '9'):
        a.append(c3)
print(len(a))
# b = [0] * 10
# for el in a:
#     b[int(el)] += 1
# for i in range(len(b)):
#     print(i, b[i])
print(Counter(a))