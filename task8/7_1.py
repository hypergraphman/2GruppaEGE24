from itertools import product

words = [''.join(word) for word in product(sorted('арсений'), repeat=6)]

k = 0
for i, word in enumerate(words, start=1):
    t = word.replace('е', 'а').replace('и', 'а').replace('с', 'р').replace('н', 'р').replace('й', 'р')
    if i % 2 == 0 and word[0] not in 'рс' and 'аа' not in t and 'рр' not in t:
        k = i
print(k)
