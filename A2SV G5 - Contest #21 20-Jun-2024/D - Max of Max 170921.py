# Problem: D - Max of Max - https://codeforces.com/gym/530187/problem/D


def check(max_value):

    for i in range(n):
        # for each start check if we can get this maximum value if we start incrementing from this index
        current_val = max_value
        cost = 0
        for j in range(i,n):
            #if the current element is the last element and it's less than the current value
            if nums[j] < current_val and j == n - 1:
                cost = k+1
                break
            if nums[j] >= current_val:
                #no need to iterate further and increment it
                break
            cost += current_val - nums[j]
            next_val = max(current_val-1,0)
            current_val = next_val  #the next element should be atmost one less than the current
        
        if cost <= k:
            return True
        
    return False
t = int(input())
for _ in range(t):
    n, k = map(int,input().split())
    nums = list(map(int,input().split()))
    left, right = max(nums), max(nums) + min(n,k)
    answer = left
    while left <= right:
        mid = left + (right - left)//2
        if check(mid):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    print(answer)
        