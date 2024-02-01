k = set()
for n in range(10, 30):
    s = '77' + '5' * n + '77'
    while '755' in s or '557' in s:
        s = s.replace('55', '5', 1)
        if '75' in s:
            s = s.replace('75', '57', 1)
        else:
            s = s.replace('57', '5')
    k.add(s)
print(len(k))