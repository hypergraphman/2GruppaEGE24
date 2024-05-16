from itertools import product

print('x y z w f')
for x, y, z, w in product((0, 1), repeat=4):
    f = int(((x <= y) or (z == x)) and (w <= z))
    print(x, y, z, w, f)