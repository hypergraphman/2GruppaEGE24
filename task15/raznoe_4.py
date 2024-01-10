arr = []
for s in range(-100, 100):
    for e in range(s, 100):
        if all(((x * x <= 20) <= (s <= x <= e)) and ((s <= x <= e) <= (x * x <= 144)) for x in range(-100, 100)):
            print(f'A принадлежит [{s}, {e}]')
            print('Длина отрезка,', e - s)
            arr.append(e - s)
print(max(arr))