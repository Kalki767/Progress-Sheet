class Solution:
    def totalNQueens(self, n: int) -> int:
        '''Approach: Backtracking. The problem asks to find the number of ways
        to put the n queens on nxn board. The problem is almost similar to the
        N queens problem. The only difference here is when we found a valid
        placement we need to increment the number of ways by 1. Otherwise we
        keep looking for a valid placement of all the queens.'''
        answer = []
        number_of_ways = 0
        columns = set()
        positive_diagonal = set()
        negative_diagonal = set()
        def backtrack(row):
            nonlocal number_of_ways
            if row == n:
                number_of_ways += 1
                return
            for col in range(n):
                if col in columns or (row+col) in positive_diagonal or (row-col) in negative_diagonal:
                    continue
                
                columns.add(col)
                positive_diagonal.add(row+col)
                negative_diagonal.add(row-col)

                backtrack(row+1)

                columns.remove(col)
                positive_diagonal.remove(row+col)
                negative_diagonal.remove(row-col)
        backtrack(0)
        return number_of_ways