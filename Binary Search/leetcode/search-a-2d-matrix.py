class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''Approach: Binary Search. The problem asks to check if a number
        exists in a 2D matrix or not. The brute force way to do this will
        be to iterate through all elements and check existence of that number
        but since we have our time constraint we need to reduce the time
        complexity. One way to do that is to think of the 2D matrix as a
        1D list and perform binary search on it. One problem that exists
        is the indexing to find the row and column after indexing we can
        take the floor division by column for the row since we are repeating
        the column we want to know on what repetition we are and for the
        column we can modulo it so we will end up having the row and column
        for the mid value. Then we can simply perform binary search on it.'''
        row , col = len(matrix), len(matrix[0])

        left, right = 0, row * col - 1
        while left <= right:
            mid = left + (right - left)//2
            number = matrix[mid//col][mid%col] #accessing the value from the matrix
            
            if number < target:
                left = mid + 1
            elif number > target:
                right = mid - 1
            else:
                return True
        return False
        #Time Complexity: O(log(m*n))
        #Space Complexity: O(1)