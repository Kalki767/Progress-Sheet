# Problem: Strange Printer II - https://leetcode.com/problems/strange-printer-ii/

class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        '''Approach:Topological Sort. The problem asks to color the current
        matrix to the target matrix but the given printer can only print
        in a rectangle. Therefore our apporach is instead of coloring the
        matrix let's uncolor the given target matrix because in that case
        we could unfold the colors that have been on one another. In that case
        we check if two colors have overlapped correctly or not. So if we end
        up uncoloring the matrix fully that means we can print the given color
        if not that means we can't. So how do we know if a color was painted
        last? We can simply check if there is no color that has overlapped
        on it if that's the case that means that color can be painted last.
        Since the printer has it's own rules to paint the color which is in
        rectangle first we find the minimum amount of rectangle that needs
        to be covered by this color and how do we do that we find the left
        most column the upper most row the right most and the down most
        cells and we build our rectangle. after we found the boundaries of
        our rectangle any color that is inside our rectangle which has a
        different color means that color has overlapped on our current color
        therefore we need to remove the overlapped one before we could
        for that one. That means before we can remove one color we need to
        remove the colors that are overlapping on it. That means one color
        has a dependency on another. And which algorithm is best for that
        topological sort. Therefore all we need to do is build the depenedencies
        and check if we can remove all colors or not if so we simply return
        true otherwise we return false.'''
        
        #Step1: initialize all the variables that are needed for later use
        graph = defaultdict(set)
        in_degree = defaultdict(int)
        colored = set()
        rows, cols = len(targetGrid), len(targetGrid[0])

        #Step2: define a function to find the boundaries of a rectangle given the color
        def find_border(row,col,color): 
            nonlocal left_col, right_col, upper_row, below_row
            for r in range(row,len(targetGrid)):
                for c in range(len(targetGrid[0])):
                    if targetGrid[r][c] == color:
                        left_col = min(left_col,c) # the left column should be minimum
                        right_col = max(right_col,c) # the right column should be maximized
                        upper_row = min(upper_row,r) # the upper row should be minimized
                        below_row = max(below_row,r) # the below row should be maximimzed

        #Step3: define a function to find overlapping colors which is build the graph
        def color_rectangle(upper_row, left_col, below_row, right_col,target):
            for row in range(upper_row,below_row+1):
                for col in range(left_col, right_col+1):
                    color = targetGrid[row][col]
                    if color != target:
                        if target not in graph[color]:
                            graph[color].add(target)
                            in_degree[target] += 1
                            colored.add(color)
                            colored.add(target)


        #Step4: iterate through the matrix and call the defined functions
        for row in range(rows):
            for col in range(cols):
                color = targetGrid[row][col]
                left_col = right_col = col
                upper_row = below_row = row
                find_border(row,col,color)
                color_rectangle(upper_row, left_col, below_row, right_col,color)

        #Step5: perform toplogical sort on the built graph
        queue = deque()
        for key in graph:
            if in_degree[key] == 0:
                queue.append(key)
        answer = []
        while queue:
            node = queue.popleft()
            answer.append(node)
            for neighbour in graph[node]:
                in_degree[neighbour] -= 1
                if in_degree[neighbour] == 0:
                    queue.append(neighbour)
        
        #if were able to touch all the colors we simply return true
        if len(answer) == len(colored):
            return True

        return False
        #Time Complexity: O(n**4)
        #Space Complexity: O(n**2)
        