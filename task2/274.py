from itertools import product

print('x y z w')
for x, y, z, w in product((0, 1), repeat=4):
    f = int((y <= x) and not z and w)
    if f:
        print(x, y, z, w)