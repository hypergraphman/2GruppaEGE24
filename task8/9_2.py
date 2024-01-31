from itertools import product

words = [''.join(word) for word in product(sorted('билств'), repeat=5)]
k = 0
for word in words:
    t = word.replace('б', 'л').replace('т', 'с').replace('в', 'с')
    if t.count('и') in [1, 3, 5] and t.count('л') == t.count('с'):
        k += 1
print(k)