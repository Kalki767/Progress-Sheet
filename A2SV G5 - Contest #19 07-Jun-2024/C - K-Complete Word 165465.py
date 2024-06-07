# Problem: C - K-Complete Word - https://codeforces.com/gym/527294/problem/C

import sys
from collections import defaultdict, Counter

def solve():
    n, k = map(int,input().split())
    s = input()
    frequency = defaultdict(Counter)
    for i in range(n):
        current_pos = i % k
        symmetry = k - current_pos - 1 #to ensure palindrome find it's counter element too
        location = min(current_pos,symmetry) # we will only be needing the first k elements so store it in minimum index
        frequency[location][s[i]] += 1

    total = 2 *(n//k) #the total means for each index that we will be looping since we decremented by half on the first loop we need to double it
    changes_needed = 0

    for i in range(k//2): #only the first half is needed because only those values appear in our dictionary
        max_frequency = max(frequency[i].values())
        changes_needed += (total - max_frequency)

    if k%2 != 0: #if our k value is odd we need to handle the middle element
        max_frequency = max(frequency[k//2].values())
        changes_needed += (n//k - max_frequency)
    print(changes_needed)
    
t = int(input())
for _ in range(t):
    solve()