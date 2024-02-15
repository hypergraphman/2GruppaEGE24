def check(n):
    for c1, c2 in zip(n, n[1:]):
        # if c1 in odd and c2 in odd or c1 in even and c2 in even:
        if (c1 in odd) != (c2 in even):
            return False
    return True



s = open('24.txt').readline().strip() + '+'
alp = '0123456789ABCDEFGHIJKLMNOPQRST'
odd = alp[1::2]
even = alp[::2]
num = s[0]
max_num = ''
for el in s:
    if el in alp:
        num += el
    else:
        if num and num[0] != '0' and check(num):
            if len(num) > len(max_num):
                max_num = num
            elif len(num) == len(max_num) and num < max_num:
                max_num = num
        num = ''
print(max_num)
