from itertools import product

words = [''.join(word) for word in product(sorted('кегэаитовру'), repeat=6)]

ans = ''
for i, word in enumerate(words, start=1):
    if i % 2 != 0 and word[0] != 'у' and word.count('к') == 2 and 'в' in word:
        ans = i

print(ans)
