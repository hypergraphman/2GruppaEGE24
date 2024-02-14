def count_first_letter(word, find):
    count = 0
    for el in word:
        if el == find:
            count += 1
        else:
            return count
    return count


words = open('24.txt').readline().strip().split('RT')
max_len = 0
for word1, word2 in zip(words, words[1:]):
    max_len = max(max_len, count_first_letter(word2, 'T') + count_first_letter(word1[::-1], 'R') + 2)
print(max_len)