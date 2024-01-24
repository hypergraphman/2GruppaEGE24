for x in range(1, 22):
    for y in range(0, 13):
        a1 = int('02305', 22) + x * 22 ** 4 + x * 22 ** 1
        a2 = int('67090', 13) + y * 13 ** 2 + y * 13 ** 0
        n = a1 - a2
        if n % 57 == 0:
            print(x + y, n // 57)
