for a in range(-100, 100):
    if all(((x <= 60) <= (x <= a)) and ((y * y <= a) <= (y <= 8)) for x in range(0, 1000) for y in range(0, 1000)):
        print(a)