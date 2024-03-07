class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''Approach: BackTracking. The problem asks to check whether or not
        the given word exists in the given board. To check if it exists we use
        backtracking. We check if we can generate the word starting from every
        index and if we manage to do that we return True. The backtracking works
        by checking if the current path is the correct path we check for the
        four directions for the next element and if one of them are true then
        we continue through that path otherwise we go back and we pop the current
        row and column from the visited so if one of the calls  to backtrack
        return true it means we have found the word.'''
        Directions = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = set()
        counter = Counter(sum(board,[]))
        for letter, value in Counter(word).items():
            if counter[letter] < value:
                return False
        rows, cols = len(board), len(board[0])

        def inbound(r,c):
            return -1 < r < rows and -1 < c < cols
        
        def backtrack(row,col,index):
            if index == len(word):#if we have reached the length of the word it means we have found a path
                return True
            #check if the current row and col is between the bound and if it's the same as the letter or if it's already visited
            if not inbound(row,col) or word[index]!= board[row][col] or (row,col) in visited:
                return False
            
            #add the current row and col to the set
            visited.add((row,col))
            for dir_x, dir_y in Directions:
                if backtrack(row + dir_x,col + dir_y,index+1):
                    return True
            #remove it from the set
            visited.remove((row,col))
            return False
        
        #check for every row and column if going through this path generates our word
        for i in range(rows):
            for j in range(cols):
                if backtrack(i,j,0):
                    return True

        return False
        #Time Complexity: O()