for a in range(-100, 100):
    is_a = True
    for x in range(0, 1000):
        for y in range(0, 1000):
            if not (((x <= 60) <= (x <= a)) and ((y * y <= a) <= (y <= 8))):
                is_a = False
                break
        if not is_a:
            break
    if is_a:
        print(a)
