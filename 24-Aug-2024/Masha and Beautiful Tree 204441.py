# Problem: Masha and Beautiful Tree - https://codeforces.com/problemset/problem/1741/D

answer = 0
def mergeSort(left, right,nums):
    global answer
    if left == right:
        return [[nums[left]]]
    elif left + 1 == right:
        if nums[left] > nums[right]:
            answer += 1
            return [[nums[right],nums[left]]]
        return [[nums[left],nums[right]]]
    mid = left + (right - left)//2
    left_subarray = mergeSort(left, mid, nums)
    right_subarray = mergeSort(mid + 1, right, nums)

    return merged(left_subarray, right_subarray)
def merged(left_subarray, right_subarray):
    global answer
    merged = []
    if left_subarray[0][0] > right_subarray[0][0]:
        answer += 1
        for value in right_subarray:
            merged.append(value)
        for value in left_subarray:
            merged.append(value)
        return merged
    for value in left_subarray:
        merged.append(value)
    for value in right_subarray:
        merged.append(value)
    return merged
def solve():
    global answer 
    answer = 0
    n = int(input())
    nums = list(map(int,input().split()))
    array = mergeSort(0, n-1, nums)
    a = [j for i in array for j in i]
    if a == sorted(a):
        print(answer)
    else:
        print(-1)
t = int(input())
for _ in range(t):
    solve()