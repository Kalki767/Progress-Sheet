# Problem: Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        '''Step1: find the rows and cols where the matrix is zero since there might 
        be duplication we will use sets to store them.'''
        zero_rows = set()
        zero_cols = set()
        rows = len(matrix)
        cols = len(matrix[0])

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    zero_rows.add(row)
                    zero_cols.add(col)
        
        #Step2: iterate through the rows and cols sequentially and update the values
        for row in zero_rows:
            for col in range(cols):
                matrix[row][col] = 0

        for col in zero_cols:
            for row in range(rows):
                matrix[row][col] = 0

        #Time Complexity: O(n*m)
        #Space Complexity: O(m+n) where m and n are length of rows and cols