# Problem: A - Split the Set - https://codeforces.com/gym/538762/problem/A

t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int,input().split()))
    counter = {0:0,1:0}
    for num in nums:
        if num % 2 == 0:
            counter[0] += 1
        else:
            counter[1] += 1
    if counter[0] == counter[1]:
        print('Yes')
    else:
        print('No')