s = open('24.txt').readline().strip().replace('L', 'X').replace('E', 'A').replace('I', 'A').replace('O', 'A').replace('U', 'A').replace('Y', 'A')
lines = s.split('X')
mx = 0
for line in lines:
    if line.count('A') >= 10:
        nums = [len(x) for x in line.split('A')]
        sums = [sum(nums[i: i + 11]) for i in range(len(nums))]
        mx = max(max(sums) + 10, mx)
    else:
        mx = max(len(line), mx)
print(mx)