for x in range(0, 101):
    for y in range(0, 41):
        for z in range(0, 11):
            f1 = z * 2 == 20
            f2 = x + y + z == 100
            f3 = y + z == 40
            if f1 and f2 and f3:
                print(x, y, z)