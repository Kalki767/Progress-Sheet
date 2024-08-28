# Problem: C - InXtracting a Subsegment - https://codeforces.com/gym/537362/problem/C

n, k = map(int,input().split())
nums = list(map(int,input().split()))
if k == 1:
    print(min(nums))
elif k == 2:
    print(max(nums[0],nums[-1]))
else:
    print(max(nums))