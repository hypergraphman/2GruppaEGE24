from fnmatch import fnmatch


for i in range(2025, 10**9, 2025):
    if fnmatch(str(i), '1?31*437?'):
        print(i, i // 2025, sep='*', end='-')
print()
a = []
for d1 in '0123456789':
    for d2 in [''] + list('0123456789'):
        for d3 in '0123456789':
            t = int(f'1{d1}31{d2}437{d3}')
            if t % 2025 == 0:
                a.append(t)
for el in sorted(a):
    print(el, el // 2025, sep='*', end='-')