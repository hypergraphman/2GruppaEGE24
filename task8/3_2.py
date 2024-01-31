from itertools import product

words = [''.join(word) for word in product(sorted('камиль'), repeat=6) if word.count('м') == 1 and word[0] != 'ь']
print(len(words))

words = [''.join(word) for word in product(sorted('камиль'), repeat=6)]
k = 0
for word in words:
    if word.count('м') == 1 and word[0] != 'ь':
        k += 1
print(k)