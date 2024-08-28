# Problem: E - Word Transformation - https://codeforces.com/gym/543431/problem/E

def solve():
    initial, final = input().split()
    left, right = len(initial) - 1, len(final) - 1
    deleted = set()
    while left >= 0 and right >= 0:
        if final[right] in deleted:
            return "NO"
        elif initial[left] != final[right]:
            deleted.add(initial[left])
        else:
            right -= 1
        left -= 1
    if right < 0:
        return "YES"
    return "NO"

t = int(input())
for _ in range(t):
    result = solve()
    print(result)
