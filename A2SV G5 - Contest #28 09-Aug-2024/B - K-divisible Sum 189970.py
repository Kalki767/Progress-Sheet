# Problem: B - K-divisible Sum - https://codeforces.com/gym/540354/problem/B

import math


def solve():
    n, k = map(int,input().split())
    diff = math.ceil(n/k)
    k *= diff
    answer = math.ceil(k/n)
    print(answer)
t = int(input())
for _ in range(t):
    solve()