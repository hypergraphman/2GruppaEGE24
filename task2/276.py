from itertools import product

print('x y z w')
# for x, y, z, w in product((0, 1), repeat=4):
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = int((w or x or y) <= ((y or z) and x or y and (w or z)))
                if not f:
                    print(x, y, z, w)