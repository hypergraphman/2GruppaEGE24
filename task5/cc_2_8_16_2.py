def f(n):
    s1 = bin(n)[2:]
    s2 = s1 + s1[-1]
    s3 = s2 + str(s2.count('1') % 2)
    return int(s3, 2)


# print(f(131))
for i in range(1, 1000):
    if f(i) > 167:
        print(f(i))
        break
