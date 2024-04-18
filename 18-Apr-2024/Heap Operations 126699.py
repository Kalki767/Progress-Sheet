# Problem: Heap Operations - https://codeforces.com/contest/681/problem/C

from heapq import heappop, heappush


n = int(input())
answer = []
min_heap = []
for _ in range(n):
    operation = input().split()
    if len(operation) == 1:
        if not min_heap:
            heappush(min_heap,1)
            answer.append(['insert', 1])
        answer.append(['removeMin'])
        heappop(min_heap)
    else:
        value = int(operation[1])
        if operation[0] == 'insert':
            answer.append(['insert', value])
            heappush(min_heap, value)
        else:
            while min_heap and min_heap[0] < value:
                heappop(min_heap)
                answer.append(['removeMin'])
            if not min_heap or min_heap[0] != value:
                answer.append(['insert', value])
                heappush(min_heap,value)
            answer.append(['getMin', value])
print(len(answer))
for ans in answer:
    print(*ans)