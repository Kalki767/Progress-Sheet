# Problem: D - Candies in the Box - https://codeforces.com/gym/538762/problem/D

def check(n,k):
    remaining = n
    vasya = 0
    while remaining > 0:
        k = min(k,remaining)
        vasya += k
        remaining -= k
        remaining -= (remaining//10)

    return vasya * 2 >= n

n = int(input())
left, right = 1, n
answer = n
while left <= right:
    mid = left + (right - left)//2
    if check(n,mid):
        answer = min(answer,mid)
        right = mid - 1
    else:
        left = mid + 1
        
print(answer)