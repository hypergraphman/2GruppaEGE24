def is_color(color):
    return set(color) <= set('0123456789ABCDEF')


def is_red(color):
    r = color[:2]
    g = color[2:4]
    b = color[4:]
    return b < r > g


s = open('24.txt').readline().strip()
k = 0
for i in range(len(s) - 6):
    if s[i] == '#':
        c = s[i + 1:i + 7]
        if is_color(c) and is_red(c):
            k += 1
print(k)
