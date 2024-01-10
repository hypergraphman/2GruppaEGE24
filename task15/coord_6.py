for a in range(1, 1000):
    if all((2 * x + 3 * y > 47) or (7 * x + y > 50) or (10 * x + y < a) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)
        break
