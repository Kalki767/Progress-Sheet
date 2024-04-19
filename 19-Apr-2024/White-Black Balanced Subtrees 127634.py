# Problem: White-Black Balanced Subtrees - https://codeforces.com/contest/1676/problem/G

import collections,sys,threading
sys.setrecursionlimit(10**9)
threading.stack_size(1<<27)
input = lambda: sys.stdin.readline().strip()

def solve():
    n = int(input())
    edges = list(map(int, input().split()))
    graph = [[] for _ in range(n + 1)]
    for index, edge in enumerate(edges):
        graph[edge].append(index + 2)
    colors = sys.stdin.readline().strip()
    counter = 0
    visited = set()
    visited.add(1)

    def dfs(node):
        nonlocal counter
        if  not graph[node]:
            return [colors[node-1]=='W', colors[node-1]=='B']
        white_count = 0
        black_count = 0
        for neighbour in graph[node]:
            result = dfs(neighbour)
            white_count += result[0]
            black_count += result[1]
        if colors[node - 1] == 'W':
            white_count += 1
        else:
            black_count += 1
        if white_count == black_count:
            counter += 1
        return [white_count, black_count]

    dfs(1)
    print(counter)

def main():
    t = int(input())
    for _ in range(t):
        solve()
if __name__ == "__main__":
    threading.Thread(target=main).start()
