class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        '''Approach: Backtracking. The problem asks to put n queens on nxn
        board so that no queen would be in a position that faces to threat to
        the other. Therefore to do that we used a concept of backtracking to
        check for every column where should we put the next queen. We called 
        backtracking on each column for each row. Therefore if I can't put a
        queen at any position then I would simply return because my for loop
        would have ended by that time for that case my row won't reach the end
        and I can go back and try another path. Finally we will return our answer
        '''
        answer = []
        text = [['.' for i in range(n)] for j in range(n)]
        columns = set()
        positive_diagonal = set()
        negative_diagonal = set()
        def backtrack(row):
            if row == n:
                res = ["".join(c) for c in text]
                answer.append(res[:])
            for col in range(n):
                if col in columns or (row+col) in positive_diagonal or (row -col) in negative_diagonal:
                    continue

                columns.add(col)
                positive_diagonal.add(row+col)
                negative_diagonal.add(row - col) 
                text[row][col] = 'Q'
                backtrack(row + 1)

                columns.remove(col)
                positive_diagonal.remove(row+col)
                negative_diagonal.remove(row - col)
                text[row][col] = '.'
        backtrack(0)
        return answer
        #Time Complexity: O(n!)
        #Space Complexity: O(n)