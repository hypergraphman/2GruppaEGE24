for a in range(1001, 2000):
    if all((x % a != 0) or (x % 36 == 0) and (x % 126 == 0) for x in range(1, 100000)):
        print(a)
        break