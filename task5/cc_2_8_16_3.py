def f(n):
    s1 = bin(n)[2:]
    s2 = s1[:-1]
    if n % 2 != 0:
        s3 = s2 + '10'
    else:
        s3 = s2 + '01'
    return int(s3, 2)


print(f(131))