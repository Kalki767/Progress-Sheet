# Problem: Maximal Square - https://leetcode.com/problems/maximal-square/


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        '''Approach: Bottom up DP. The problem asks to find the maximal area
        of square of 1's that we could have. The basic intution here is how
        can we make a square. The side of the squares are equal by law. So
        let's use that fact to our cause. To know the side of the square that
        will be made including the current cell we need to check with our
        neighbours because they obviously will be part of our square. The
        minimum square that's greater than one is size 2, When we have a
        square with size 2 we will have the row and neighbour columns and
        the diagonal. So if we know the minimum side out of the three cells
        that means our current cell can extend till that and make square.
        Therefore all we have to do is at each step find the minimum side
        among the three and add 1 to it because a cell by itself is a square.
        The given input is string of 0's and 1's so we need to convert that
        to integers for ease of use. Here the cells that are at the corners
        can have a maximum of 1 and a minimum of 0 side so we need to take
        into account that also. Lastly we updated the input which is not
        recommended but we have optimized the space since we operated on
        the given input itself.'''

        #Step1: handle edge cases like when the matrix length is 0
        if not matrix :
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        max_side = 0
        
        #Step2: Convert matrix to integer for easier calculations
        for row in range(rows):
            for col in range(cols):
                matrix[row][col] = int(matrix[row][col])
                if matrix[row][col] == 1:
                    max_side = 1
        
        #Step3: Start from 1 to avoid index out of range error
        for row in range(1, rows):
            for col in range(1, cols):
                #the current cell will only get updated if it's not zero which means it's one
                if matrix[row][col] == 1:
                    matrix[row][col] = min(matrix[row-1][col], matrix[row][col-1], matrix[row-1][col-1]) + 1
                    max_side = max(max_side, matrix[row][col])
        
        # since we are asked the area return the square of the maximum side
        return max_side ** 2

        #Time Complexity: O(rows*cols)
        #Space Complexity: O(1) since we update the given input if not it would be the same as the time complexity