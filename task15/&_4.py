for a in range(45, 65 + 1):
    if all(not ((((x & 30 != 0) <= (x & 10 != 0)) or (x & a != 0)) <= ((x & 10 == 0) and (x & a == 0) and (x & 21 != 0))) for x in range(1, 100000)):
        print(a)