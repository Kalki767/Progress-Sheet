# Problem: B - Excluded Integer Sum Problem - https://codeforces.com/gym/531455/problem/B

def solve():
    n, k, x = map(int,input().split())
    if x != 1:
        print('YES')
        print(n)
        result = [1]*n
        print(*result)
    elif k == 1:
        print('NO')
    elif k == 2 and n % 2 != 0:
        print('NO')
    else:
        print('YES')
        print(n//2)
        result = [2]*((n//2) - 1)
        if n % 2 == 0:
            result.append(2)
        else:
            result.append(3)
        print(*result)
t = int(input())
for _ in range(t):
    solve()