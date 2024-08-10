# Problem: E - Beef in M.A.A.D City - https://codeforces.com/gym/538762/problem/E

from collections import deque


def solve():
    n, m, v = map(int,input().split())
    #build the graph
    graph = [[] for _ in range(n)]
    degree = [0 for _ in range(n)]
    for _ in range(n):
        a,b = map(int,input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
        degree[a-1] += 1
        degree[b-1] += 1
    
    queue = deque()
    for i in range(n):
        if degree[i] == 1:
            queue.append(i)
    
    removed = set()
    while queue:
        node = queue.popleft()
        removed.add(node)

        for child in graph[node]:
            degree[child] -= 1
            if degree[child] == 1:
                queue.append(child)
    
    reached = [0 for _ in range(n)]
    queue.append(m-1)
    queue.append(v-1)
    reached[m-1] = 1
    reached[v-1] = 2
    while queue:
        boundary = len(queue)
        for _ in range(boundary):
            node = queue.popleft()
            for child in graph[node]:
                if reached[child] == 0:
                    queue.append(child)
                    reached[child] = reached[node]
    first = 0
    for i in range(n):
        if i not in removed and reached[i] == 2:
            first = 1
    if first == 1 and v != m:
        print('YES')
    else:
        print('NO')

t = int(input())
for _ in range(t):
    solve()
