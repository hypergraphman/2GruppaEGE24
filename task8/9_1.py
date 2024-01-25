from itertools import product

words = [''.join(word) for word in product(sorted('ластик'), repeat=5)]

k = 0
for i, word in enumerate(words, start=1):
    t = word.replace('и', 'а').replace('с', 'л').replace('т', 'л').replace('к', 'л')
    if 'каска' <= word and i <= 4045 and 'аа' not in t and 'лл' not in t:
        k += word.count('и')
print(k)
