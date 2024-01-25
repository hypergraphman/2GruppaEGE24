for x in range(1, 16):
    a1 = int('01310131', 16) + x * 16 ** 7 + x * 16 ** 3
    a2 = int('1004000', 16) + x * 16 ** 0
    n = a1 + a2
    if n % 15 == 0:
        print(x, n // 15)
