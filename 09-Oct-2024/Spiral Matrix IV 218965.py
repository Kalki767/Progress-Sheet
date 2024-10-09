# Problem: Spiral Matrix IV - https://leetcode.com/problems/spiral-matrix-iv/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        #function to check if the row and column are still inbound
        def inbound(row,col):
            return 0 <= row < m and 0 <= col < n
        r, c = 0,1
        matrix = [[-1 for _ in range(n)] for _ in range(m)]
        row, col = 0,0
        visited = set()
        temp = head

        #iterate over the linked list
        while temp:
            matrix[row][col] = temp.val
            visited.add((row,col))
            #if it goes out of bound or have been updated before then change the direction
            if not inbound(row + r,col + c) or (row+r, col+c) in visited:
                r *= -1
                r, c = c,r
            row, col = row + r, col + c
            temp = temp.next

        return matrix 
        #Time Complexity: O(m*n)
        #Space Complexity: O(m*n)