def f(s1, s2, c, m):
    if (s1 + s2) >= 150:
        return c % 2 == m % 2
    if c == m:
        return 0
    moves = [f(s1 + 2, s2, c + 1, m),
             f(s1, s2 + 2, c + 1, m),
             f(s1 * 3, s2, c + 1, m),
             f(s1, s2 * 3, c + 1, m)]
    return any(moves) # if (c + 1) % 2 == m % 2 else all(moves)


for s in range(1, 134):
    for m in range(1, 5):
        if f(16, s, 0, m):
            if m == 4:
                print(s, m)
            break
