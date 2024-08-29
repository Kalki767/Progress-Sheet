# Problem: C - Removal Hack - https://codeforces.com/gym/534160/problem/C

'''Approach: The problem asks to find the order of deletion for the given rules which is if a vertex doesn't respect it's parents and none
of it's children respect it we must delete it. Therefore all we need to do is find those vertexes. How? Upon accepting the inputs if
the current vertex respects it's parent that means atleast one child has respected it's parent so we mark that as true and since this
child respects it's parent we will also mark it as true. Finally we collect vertices where they don't respect their parent and none of
their children respected them and we sort that value.'''

n = int(input())
respected = [False for _ in range(n)]
respects = [False for _ in range(n)]
for i in range(n):
    p, c = map(int,input().split())
    if c == 0:
        if p != -1:
            respected[p-1] = True
        respects[i] = True
answer = []
for i in range(n):
    if respected[i] == False and respects[i] == False:
        answer.append(i+1)
if answer:
    answer.sort()
    print(*answer)
else:
    print(-1)

#Time Complexity: O(n)
#Space Complexity: O(n)