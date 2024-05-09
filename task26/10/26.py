n, *data = map(int, open('26.txt'))
data = sorted(set(data), reverse=True)
print(data)
b = [data[0]]
for box in data:
    if b[-1] - 3 >= box:
        b.append(box)
print(len(b), b[-1])