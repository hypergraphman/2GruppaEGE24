f = open('24.txt')
s = f.readline().strip() + 'x'
max_number = 0
number = ''
for c in s:
    if c in '0123456789':
        number += c
    else:
        if number and set(number) <= set('24680') and int(number) > max_number:
            max_number = int(number)
        number = ''
print(max_number)
