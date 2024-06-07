# Problem: D - Rizzler's String - https://codeforces.com/gym/527294/problem/D

s = input()
answer = 0
last_b = 0
mod = 10**9 + 7
for i in range(len(s)):
    if s[i] == 'b':
        last_b = answer
    elif s[i] == 'a':
        answer += last_b + 1
        answer %= mod
print(answer)