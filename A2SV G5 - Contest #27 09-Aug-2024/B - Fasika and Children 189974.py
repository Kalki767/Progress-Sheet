# Problem: B - Fasika and Children - https://codeforces.com/gym/538762/problem/B

import math
n,m = map(int,input().split())
candies = list(map(int,input().split()))
for i in range(n):
    curr = math.ceil(candies[i]/m)
    candies[i] = curr
answer = 0
for i in range(n):
    if candies[i] >= candies[answer]:
        answer = i
print(answer+1)