# Problem: B - Grid Path - https://codeforces.com/gym/524965/problem/B

def solve():
    n, m, k = map(int,input().split())
    if (n-1) + n*(m-1) == k:
        print('YES')
    else:
        print('NO')
t = int(input())
for _ in range(t):
    solve()