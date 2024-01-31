from itertools import permutations

words = [''.join(word) for word in permutations('равиль', r=6)]
s = set()
for word in words:
    if word[0] != 'ь' and 'аь' not in word and'иь' not in word:
        s.add(word)
print(len(s))