# Problem: B - Distinct Digits - https://codeforces.com/gym/530187/problem/B

import math


def solve():
    s = int(input())
    answer = []
    current = 9
    while s > current:
        answer.append(current)
        s -= current
        current -= 1
    answer.append(s)
    answer.reverse()
    res = 0
    for i in answer:
        res = res * 10 + i
    print(res)
t = int(input())
for _ in range(t):
    solve()