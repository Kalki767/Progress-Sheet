# Problem: Longest Increasing Path in a Matrix - https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        '''Approach: Topological Sort using Kahn's Algorithm. The problem
        asks to find the length of the longest increasing path. That means
        if we have the paths of each increasing path then we can take the 
        maximum using level order dfs tarversal. Therefore all we need to do
        is build DAG for each cell then we can move starting from cells which
        have an indegree of zero. Why topological sorting because it gives
        linear ordering and specially for this case when we say the in degree
        is zero there is no element that can come before that element because
        if we start our bfs from other nodes we might not get the longest 
        path. Therefore start from in degree zero and move as one would in
        topological sorting.'''

        #Step1: bulid a DAG using the inequality and count the indegrees
        graph = defaultdict(list)
        rows, cols = len(matrix), len(matrix[0])
        in_degree = [[0 for _ in range(cols)] for _ in range(rows)]
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        #Step2: define a function to check if we have run out of bound or not
        def inbound(row,col):
            return 0 <= row < rows and 0 <= col < cols
        
        #Step3: count the in degrees to each cell that's the number of cells that are less than to it which could be a maximum of 4
        for row in range(rows):
            for col in range(cols):
                for x, y in directions:
                    new_row = row + x
                    new_col = col + y

                    #check if we are still inbound and it's valid cell
                    if inbound(new_row,new_col) and matrix[new_row][new_col] > matrix[row][col]:
                        in_degree[new_row][new_col] += 1
        
        #Step3: add the cells which have an in degree zero into the queue
        queue = deque()
        for row in range(rows):
            for col in range(cols):
                if in_degree[row][col] == 0:
                    queue.append((row,col))
        
        #Step4: perform topo sort using kahn's algorithm and increment the length by one at each step
        level = 0
        while queue:
            length = len(queue)
            for _ in range(length):
                row, col = queue.popleft()
                for x, y in directions:
                    new_row = row + x
                    new_col = col + y

                    #to check if the next cell is valid using the given rukes
                    if inbound(new_row,new_col) and matrix[new_row][new_col] > matrix[row][col]:
                        in_degree[new_row][new_col] -= 1
                        if in_degree[new_row][new_col] == 0:
                            queue.append((new_row,new_col))
            level += 1

        return level
        #Time Complexity: O(n*m) where n is length of rows and m is length of cols
        #Space Complexity: O(n*m) for in degree and queue