arr = []
for s in range(-100, 100):
    for e in range(s, 100):
        if all(((s <= x <= e) <= (x * x <= 100)) and ((x * x <= 64) <= (s <= x <= e)) for x in range(-100, 100)):
            print(f'A принадлежит [{s}, {e}]')
            print('Длина отрезка,', e - s)
            arr.append(e - s)
print(min(arr))