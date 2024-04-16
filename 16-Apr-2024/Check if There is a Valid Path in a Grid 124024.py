# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        '''Approach: BFS. The problem asks if there is a valid path in the
      given grid. We can use both traversal ways but here we will be using
      bfs. To solve this problem first we need to know where which road will
      take us and after that we will also need to check if the road the we
      arrived at can accept our initial road. Therefore we need to creat two
      maps one for choosing where we can go with the current node one to check
      if we can continue comin from that road. After that we can perform simple
      bfs traversal and if at any point we arrive at the destination we will
      return true otherwise we return false.'''
        directions = {
        1: [(0,-1),(0,1)],
        2: [(-1,0),(1,0)],
        3: [(0,-1),(1,0)],
        4: [(0,1),(1,0)],
        5: [(0,-1),(-1,0)],
        6: [(0,1),(-1,0)]
        }
        destinations = {
         (0, 1):{1, 3, 5},
        (0, -1):{1, 4, 6},
        (1, 0):{2, 5, 6},
        (-1, 0):{2, 3, 4}
        }
    
        row_length, col_length = len(grid), len(grid[0])
        queue = deque()
        queue.append((0,0))
        visited = set(queue)

        def inbound(row,col):
            return 0 <= row < row_length and 0 <= col < col_length

        while queue:
            row,col = queue.popleft()
            if row == row_length - 1 and col == col_length - 1:
                return True
            for x,y in directions[grid[row][col]]:
                new_row = row + x
                new_col = col + y
                if inbound(new_row,new_col) and (new_row,new_col) not in visited and grid[new_row][new_col] in destinations[(x,y)]:
                    queue.append((new_row,new_col))
                    visited.add((new_row,new_col))
        return False
        #Time Complexity: O(n*m)
        #Space Complexity: O(n*m)