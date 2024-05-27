# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        '''Approach: Graph. The problem asks to identify a unique winner based
        on the given rules if there is any otherwise print -1. To solve this
        problem a team is supposed to be the winner if there is no team that
        is stronger than it. That means the indegree of that team is zero.
        Therefore all we have to do is count the indegrees of the teams and
        if there is only one team that has an indegree of zero return that
        team otherwise return -1'''

        in_degree = [0 for _ in range(n)]
        answer = []
        for u, v in edges:
            in_degree[v] += 1
        
        for i in range(0,n):
            if in_degree[i] == 0:
                answer.append(i)
                
        if len(answer) > 1:
            return -1
        return answer[0]

        #Time Complexity: O(n)
        #Space Complexity: O(n)