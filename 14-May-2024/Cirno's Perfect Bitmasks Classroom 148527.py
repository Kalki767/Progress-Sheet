# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

def solve():
    n = int(input())
    if n & n-1 == 0:
        if n != 1:
            print(n+1)
            return
        print(3)
    else:
        length = n.bit_length()
        for i in range(length):
            if n & 1 << i and n ^ 1 << i:
                print(1<<i)
                return
t = int(input())
for _ in range(t):
    solve()
        
            