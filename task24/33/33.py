lines = open('24.txt').readline().strip().split('Q')
nums = [len(line) for line in lines]
sums = [sum(nums[i: i + 4]) for i in range(len(nums) - 3)]
print(max(sums) + 3)
