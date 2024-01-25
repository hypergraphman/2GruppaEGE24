from itertools import product

words = [''.join(word) for word in product(sorted('кегэаитов'), repeat=6)]

k = 0
for i, word in enumerate(words, start=1):
    if i % 2 == 0 and word[0] != 'т' and word.count('е') == 2:
        k += 1
print(k)
