lines = open('24.txt').readline().strip().split('W')
nums = [len(line) for line in lines]
sums = [sum(nums[i: i + 99]) for i in range(len(nums) - 98)]
print(min(sums) + 100)

