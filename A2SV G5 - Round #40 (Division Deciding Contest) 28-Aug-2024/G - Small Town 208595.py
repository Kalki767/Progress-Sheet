# Problem: G - Small Town - https://codeforces.com/gym/543431/problem/G

from bisect import bisect_right


def solve():
    '''Approach: Binary Search. The problem asks to find the minimum amount of time each person has to wait to get their woods done.
    for this case this means that this time will be the maximum amount of time among each people waiting. This means we need to partition
    the woods into three in a way it would make the time taken minimum. So anyways we need to partition the woods for the carvers to
    work on therefore what if we check if the maximum waiting of a person is t time then how much carvers need to work on it. If we
    find that number we can simply check if it's less than or equal to 3 or not if not then the time is not enough otherwise we opt
    for a minimum one. But how do we know how to partition the woods for the carvers. For that case we need to find the right boundary
    of one carver because if the partition is in the middle it can extend to the right and to the left so we found our formula and
    we can bisect right that thing since we don't want to exclude repetitions.'''
    n = int(input())
    woods = list(map(int,input().split()))
    woods.sort()
    left, right = 0, woods[-1] - woods[0]
    ans = float('inf')

    #a function for checking if a given time is feasible
    def check(time):
        left = 0
        carvers = 0
        while left < len(woods):
            right = 2*time + woods[left] #the next carver partition
            left = bisect_right(woods,right)
            carvers += 1
        return carvers
    
    while left <= right:
        mid = left + (right - left)//2
        if check(mid) <= 3: #check for the number of carvers and update the answer
            ans = min(ans,mid)
            right = mid - 1
        else:
            left = mid + 1

    print(ans)
    
t = int(input())
for _ in range(t):
    solve()