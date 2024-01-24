t = f'{12 * 32 ** 2 + 16 ** 3 - 2 ** 5 + 12:o}'
k = 0
for el in t:
    if el in '13579':
        k += 1
print(k)
