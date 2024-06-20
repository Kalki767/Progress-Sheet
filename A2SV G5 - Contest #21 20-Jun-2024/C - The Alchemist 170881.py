# Problem: C - The Alchemist - https://codeforces.com/gym/530187/problem/C

from collections import defaultdict, deque


def solve():
    graph = defaultdict(list)

    n, k = map(int,input().split())
    potions = [0] + list(map(int,input().split()))
    k_index = set(map(int,input().split()))

    answer = [0 for _ in range(n+1)]
    in_degrees = [0 for _ in range(n+1)]
    future = [0 for _ in range(n+1)]

    for i in range(1,n+1):
        l = list(map(int,input().split()))
        degree, edges = l[0], l[1:]
        if i in k_index:
            continue
        in_degrees[i] = degree
        for edge in edges:
            graph[edge].append(i)
    
    queue = deque()
    for node in range(1,n+1):
        if node in k_index:
            queue.append(node)
        elif in_degrees[node] == 0:
            answer[node] = potions[node]
            queue.append(node)
    
    while queue:
        node = queue.popleft()
        for child in graph[node]:
            in_degrees[child] -= 1
            future[child] += answer[node]
            if in_degrees[child] == 0:
                answer[child] = min(potions[child],future[child])
                queue.append(child)
    print(*answer[1:])
    
t = int(input())
for _ in range(t):
    solve()