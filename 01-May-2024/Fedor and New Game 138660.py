# Problem: Fedor and New Game - https://codeforces.com/contest/467/problem/B

n, m, k = map(int,input().split())
soldiers = []
for _ in range(m+1):
    sol = int(input())
    soldiers.append(sol)
answer = 0
for index in range(m):
    sol = soldiers[index]
    xor = sol ^ soldiers[-1]
    diff = 0
    while xor > 0:
        if xor & 1 == 1:
            diff += 1
        xor >>= 1
    if diff <= k:
        answer += 1
print(answer)