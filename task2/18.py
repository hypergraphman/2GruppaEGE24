print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = int((not y or z or w) == (not z and w and x))
                if f:
                    print(x, y, z, w)