for p in range(9, 100):
    for x in range(0, p):
        for y in range(1, p):
            for z in range(0, p):
                a1 = 6 * p ** 3 + x * p ** 2 + 5 * p ** 1 + x * p ** 0
                a2 = 1 * p ** 3 + x * p ** 2 + 6 * p ** 1 + 5 * p ** 0
                r = y * p ** 3 + 8 * p ** 2 + z * p ** 1
                if a1 + a2 == r:
                    print(x * p ** 2 + y * p + z)
                    print(x, y, z, p)
