f = open('24.txt')
s = f.readline().strip() + 'x'
max_number = 0
numer = ''
for c in s:
    if c in '0123456789':
        numer += c
    else:
        if numer and numer[-1] in '13579' and int(numer) > max_number:
            max_number = int(numer)
        numer = ''
print(max_number)
