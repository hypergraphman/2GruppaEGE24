for n in range(21, 100):
    k = 0
    for x in range(0, 100):
        if ((not (70 <= x <= 90)) <= (15 <= x <= 50)) and ((not (20 <= x <= n)) <= (70 <= x <= 90)):
            k += 1
    if k > 35:
        print(n)