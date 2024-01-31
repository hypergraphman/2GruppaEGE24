from itertools import product

words = [''.join(word) for word in product(sorted('карим'), repeat=5)]
k = 0
for word in words:
    t = word.replace('и', 'а')
    if t.count('ка') == t.count('к') and word.count('к') == 1:
        print(word)
        k += 1
print(k)