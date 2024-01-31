from itertools import permutations

words = [''.join(word) for word in permutations('перевыборы', r=10)]
s = set()
for word in words:
    t = word.replace('о', 'е').replace('ы', 'е').replace('р', 'п').replace('в', 'п').replace('б', 'п')
    if 'ее' not in t and 'пп' not in t:
        s.add(word)
print(len(s))