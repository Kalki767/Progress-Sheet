# Problem: Alien Dictionary ( GeeksforGeeks ) - https://www.geeksforgeeks.org/problems/alien-dictionary/1

from collections import defaultdict, deque
class Solution:
    def findOrder(self,alien_dict, N, K):
    # code here
        graph = defaultdict(list)
        in_degree = {chr(i+97):0 for i in range(K)}
        for i in range(1, N):
            word1 = alien_dict[i-1]
            word2 = alien_dict[i]
            result = self.findDifference(word1,word2)
            if not result:
                continue
            else:
                char1 = result[0]
                char2 = result[1]
                graph[char1].append(char2)
                in_degree[char2] += 1
        queue = deque()
        for key, val in in_degree.items():
            if val == 0:
                queue.append(key)
        answer = []
        while queue:
            current = queue.popleft()
            answer.append(current)
            for neighbour in graph[current]:
                in_degree[neighbour] -= 1
                if in_degree[neighbour] == 0:
                    queue.append(neighbour)
        return "".join(answer)         
            
    def findDifference(self,word1,word2):
        index = 0
        while index < len(word1) and index < len(word2):
            if word1[index] != word2[index]:
                return [word1[index], word2[index]]
            index += 1
        return []
    