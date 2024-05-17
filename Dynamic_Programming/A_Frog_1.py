n = int(input())
nums = list(map(int,input().split()))

dp = [float('inf') for _ in range(n)]
dp[-1] = 0
for index in range(n-2,-1,-1):
    one_step = abs(nums[index+1]-nums[index]) + dp[index+1]
    two_step = float('inf')
    if index + 2 < len(nums):
        two_step = abs(nums[index+2]-nums[index]) + dp[index+2]
    dp[index] = min(one_step,two_step)
print(dp[0])

