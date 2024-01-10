for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            print(int(a and (c or not (not b or c)) or b and not (a and c)))