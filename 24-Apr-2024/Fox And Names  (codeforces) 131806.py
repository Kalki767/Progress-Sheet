# Problem: Fox And Names  (codeforces) - https://codeforces.com/contest/510/problem/C

from collections import defaultdict, deque
answer = []
def solve():
    n = int(input())
    def differ(word1,word2):
        index = 0
        while index < len(word2) and index < len(word1):
            if word1[index] != word2[index]:
                return [word1[index], word2[index]]
            index += 1
        if index < len(word1):
            return [-1]
        return []
    characters = set()
    words = []
    in_degree = defaultdict(int)
    graph = defaultdict(list)
    for _ in range(n):
        word = input()
        words.append(word)
    for i in range(n-1):
        word1 = words[i]
        word2 = words[i+1]
        if word1[0] == word2[0]:
            result = differ(word1,word2)
            if not result:
                continue
            elif result[0] == -1:
                return False
            else:
                graph[result[0]].append(result[1])
                in_degree[result[1]] += 1
                characters.add(result[0])
                characters.add(result[1])
        else:
            graph[word1[0]].append(word2[0])
            in_degree[word2[0]] += 1
            characters.add(word1[0])
            characters.add(word2[0])
    queue = deque()
    for key, value in graph.items():
        if in_degree[key] == 0:
            queue.append(key)
    while queue:
        node = queue.popleft()
        answer.append(node)
        for neighbour in graph[node]:
            in_degree[neighbour] -= 1
            if in_degree[neighbour] == 0:
                queue.append(neighbour)
    if len(answer) == len(characters):
        return True
    return False
result = solve()
if not result:
    print('Impossible')
else:
    value = set(answer)
    start = 97
    for index in range(26):
        character = chr(start+index)
        if  character not in value:
            answer.append(character)
    print("".join(answer))