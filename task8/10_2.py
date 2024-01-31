from itertools import product

words = [''.join(word) for word in product(sorted('01234'), repeat=3)]
k = 0
for word in words:
    if word[0] != '0' and word[0] > word[1] > word[2]:
        k += 1
        print(word)
print(k)