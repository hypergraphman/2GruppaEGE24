f = open('26.txt')
# f = open('test.txt')
n, m, *a = map(int, f.read().split())
s = m
truck = []
cargo = []
count_cargo = 0
for el in a:
    if 170 <= el <= 180:
        m -= el
        count_cargo += 1
    else:
        cargo.append(el)
cargo.sort(reverse=True)
while sum(truck) + cargo[-1] <= m:
    truck.append(cargo.pop())
count_cargo += len(truck)
print(count_cargo)
truck.sort(reverse=True)
for i in range(len(truck)):
    cargo.append(truck.pop(i))
    cargo.sort(reverse=True)
    for j in range(len(cargo)):
        if cargo[j] + sum(truck) <= m:
            truck.insert(i, cargo.pop(j))
            break
print(sum(truck) + s - m)
