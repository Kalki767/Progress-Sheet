# Problem: C - Permutation Sorting - https://codeforces.com/gym/538762/problem/C

def solve():
    n = int(input())
    permutation = list(map(int,input().split()))
    previous = set()
    answer = 0
    for num in permutation:
        if num+1 in previous:
            answer += 1
        previous.add(num)
    print(answer)

t = int(input())
for _ in range(t):
    solve()