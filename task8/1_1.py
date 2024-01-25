from itertools import product

words = [''.join(word) for word in product(sorted('снегурочка'), repeat=5)]
k = 0
for word in words:
    if 'ручка' <= word <= 'чукча':
        k += 1
print(k)