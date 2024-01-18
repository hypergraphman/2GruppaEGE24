def f(n):
    s1 = bin(n)[2:].rjust(8, '0')
    # s1 = f'{n:0>8b}'
    s2 = ''
    for c in s1:
        if c == '1':
            s2 += '0'
        else:
            s2 += '1'
    return int(s2, 2)


for n in range(1, 256):
    if f(n) - n == 131:
        print(n)