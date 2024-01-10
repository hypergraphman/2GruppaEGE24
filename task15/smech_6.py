for a in range(1, 1000):
    if all(((abs(45 - x) <= 10) and (not (52 <= x <= 72))) <= ((x % 3 == 0) or ((x & a != 0) <= (x in (36, 42, 49, 50)))) for x in range(1, 100000)):
        print(a)
        break