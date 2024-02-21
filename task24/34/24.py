lines = open('24.txt').readline().strip().split('VLADIMIR')
nums = [len(line) for line in lines]
sums = [sum(nums[i: i + 4]) for i in range(len(nums) - 3)]
print(min(sums) + 8 * 5)

