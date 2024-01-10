for a in range(1, 1000):
    if all((a >= x) and (a >= y) or ((x / 20 + y / 60) != 131131) for x in range(0, 10000) for y in range(0, 10000)):
        print(a)
