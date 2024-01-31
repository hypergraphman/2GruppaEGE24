from itertools import product

words = [''.join(word) for word in product(sorted('licey'), repeat=4)]
print(len(words))
