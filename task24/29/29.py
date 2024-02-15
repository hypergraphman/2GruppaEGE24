s = open('24.txt').readline().strip() + '+'
alp = '0123456789ABCDEFGHIJ'
num = ''
max_num = '0'
for el in s:
    if el in alp:
        num += el
    else:
        if num and num[0] != '0' and int(num, len(alp)) % 2 == 0 and int(num, len(alp)) > int(max_num, len(alp)):
            max_num = num
        num = ''
print(max_num)