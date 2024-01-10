f1 = ''
f2 = ''
for a in 0, 1:
    for b in 0, 1:
        f1 += str(int((a or b) and (not a or not b)))
        f2 += str(int(a != b))
print(f1)
print(f2)