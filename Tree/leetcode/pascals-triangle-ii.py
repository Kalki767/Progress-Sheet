class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        '''Approach: Recursion. The problem asks to find the pascal elements
        at the given row. To find that we call a function called pascal
        recursively with a base cased of 0 and 1. Therefore if the row is
        different from our base case then we update the list from our base
        case and return it to our caller. In that case we will end up with
        the desired solution.
        '''
        def pascal(row):
            if row == 0:
                return [1]
            elif row == 1:
                return [1,1]
            else:
                last_row = pascal(row-1)
                answer = [1]
                for index in range(1,len(last_row)):
                    answer.append(last_row[index-1]+last_row[index])
                answer.append(1)
                return answer
        return pascal(rowIndex)
        '''Time Complexity: O(n*n) where the first n is to analyze our answer
        and the second n is for function call'''
        #Space Compplexity: O(n*n) for stack calling and for storing the list