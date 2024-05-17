n = int(input())
nums = list(map(int,input().split()))
memory = {}

def dp(index):
    if index == len(nums)-1:
        return 0
    if index not in memory:
        one_step = abs(nums[index+1]-nums[index]) + dp(index+1)
        two_step = float('inf')
        if index + 2 < len(nums):
            two_step = abs(nums[index+2]-nums[index]) + dp(index+2)
        memory[index] = min(one_step,two_step)
    return memory[index]
print(dp(0))
