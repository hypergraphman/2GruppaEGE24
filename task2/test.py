from itertools import product

for z, w in product((0, 1), repeat=2):
    f1 = int(not (z <= w))
    f2 = int((not z) <= w)
    print(f1, f2)