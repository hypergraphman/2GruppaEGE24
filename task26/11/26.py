f = open('26.txt')
n = int(f.readline())
data = []
for _ in range(n):
    d, t = map(int, f.readline().split())
    data.append((d, d - 2 * t))
data.sort(key=lambda x: -x[1])
print(data)
p = [data[0]]
for d, in_d in data:
    pd, pin_d = p[-1]
    if pin_d - 3 >= d:
        p.append((d, in_d))
print(len(p))
pin_d = p[-2][1]
data.sort()
mx = 0
for d, in_d in data:
    if pin_d - 3 >= d > mx:
        mx = d
print(mx)


