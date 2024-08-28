# Problem: F - OR Encryption - https://codeforces.com/gym/543431/problem/F

def solve():
    n = int(input())
    matrix = []
    for _ in range(n):
        cur = list(map(int,input().split()))
        matrix.append(cur)
    setted = (2**30) - 1
    locks = [setted for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            locks[i] &= matrix[i][j]
            locks[j] &= matrix[i][j]
    for i in range(n):
        for j in range(n):
            if i != j and matrix[i][j] != (locks[i] | locks[j]):
                return 'NO'
    return locks
t = int(input())
for _ in range(t):
    result = solve()
    if result == 'NO':
        print(result)
    else:
        print('YES')
        print(*result)