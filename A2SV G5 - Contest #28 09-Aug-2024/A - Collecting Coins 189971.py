# Problem: A - Collecting Coins - https://codeforces.com/gym/540354/problem/A

t = int(input())
for _ in range(t):
    a,b,c,n = map(int,input().split())
    val = (a+b+c+n)
    if val % 3 == 0 and (val//3 >= max(a,b,c)):
        print('YES')
    else:
        print('NO')