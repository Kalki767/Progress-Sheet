# Problem: Convert 1D Array Into 2D Array - https://leetcode.com/problems/convert-1d-array-into-2d-array/

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        '''Approach: BruteForce. Check if the total number of elements of the 2d array
        is different from the elements of the original then the matrix cannot be built.
        Otherwise iterate through the original and build the matrix.'''
        if m*n != len(original):
            return []
        answer = []
        for index in range(0,len(original),n):
            cur = []
            for i in range(index,index+n):
                cur.append(original[i])
            answer.append(cur)
        return answer
        #Time Complexity: O(n*m)
        #Space Complexity: O(n)