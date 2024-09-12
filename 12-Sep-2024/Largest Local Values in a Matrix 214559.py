# Problem: Largest Local Values in a Matrix - https://leetcode.com/problems/largest-local-values-in-a-matrix/

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        '''Approach: Matrix. The problem asks to find the maxlocal for each grid which
        is three by three grid. To solve this problem we can easily find each grid for
        every row and find the max of that grid and append it to our answer. To find
        the maximum we can use a helper function for clean code'''

        #helper function to find the maximum of a 3*3 grid
        def helper(i,j):
            maximum = float('-inf')
            for row in range(i,i+3):
                for col in range(j,j+3):
                    maximum = max(maximum,grid[row][col])
            return maximum
        
        #iterate through the grid and build our answer
        answer = []
        rows = len(grid)
        cols = len(grid[0])
        for row in range(rows-2):
            cur = []
            for col in range(cols-2):
                maxi = helper(row,col)
                cur.append(maxi)
            answer.append(cur)
        return answer
        
        #Time Complexity: O(m*n) m is the row length and n is the column length
        #Space Complexity: O(1)