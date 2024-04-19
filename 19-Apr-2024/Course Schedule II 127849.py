# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''Approach: Topological Sorting. The problem asks if it's possible to
        finish all courses and return that order. To check if it's possible then
        we need to traverse through each prerequisite. The approach is topological
        sorting since we need the orders but there are two implementations Bfs
        and Dfs. Here we will use the dfs implementation all we have to do is
        traverse depth for each node and if we detect a cycle at any point just
        return false if not up on reaching a leaf node which is a node with no
        child then add it to the answer. Since the graph might be disconnected
        we might need to call the dfs multiple times therefore we need to
        make sure that none of these calls will have a cycle.'''
        answer = []
        colors = [0 for _ in range(numCourses)]
        graph = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            graph[pre].append(course)
        def dfs(course):
            #check if we have detected cycle
            if colors[course] == 1:
                return False
            colors[course] = 1 #to mark that we are currently proccesing this node
            for neighbour in graph[course]:
                if colors[neighbour] == 2: #if the node is already processed skip it
                    continue
                if not dfs(neighbour): #if one of the child has cycle no need to traverse
                    return False
            colors[course] = 2
            answer.append(course) #if we finish proccesing it append it to our answer
            return True
        for i in range(numCourses):
            if colors[i] == 0: #to handle disconnected graph
                if not dfs(i):
                    return []
        #since the above traverse will result in reversed order we need to reverse it
        return reversed(answer)
        #Time Complexity: O(V+E)
        #Space Complexity: O(V) for call stack