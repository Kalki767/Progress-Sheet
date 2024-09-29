# Problem: Find Missing Observations - https://leetcode.com/problems/find-missing-observations/

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        '''Approach: Math. The problem asks to find the remaining rolls if the total
        mean is given and n and m are given. The first thing that we need to do is
        find the remaining sum to get the mean given on all rolls. After finding the
        remaining sum we need to know the value that each will have. To know that we
        can simply divide the remaining sum by n. If on average the remaining value
        is either greater than 6 or less than or equal to 0 then we will simply
        return [] otherwise we build our answer and we add the remaining ones on the
        answer.'''
        remaining_sum = mean * (n+len(rolls)) - sum(rolls)

        #handling each edge case 
        if remaining_sum/n > 6 or remaining_sum <= 0:
            return []
        final = remaining_sum//n
        if final == 0: # if the final is 0 that means we can't build the answer
            return []
        
        #build the answer using the final that was calculated
        answer = [final for _ in range(n)]
        cur = remaining_sum % n
        index = 0

        #iterate to add the remaining values on the answer
        while cur > 0:
            mini = 6 - answer[index]
            mini = min(mini,cur)
            answer[index] += mini
            cur -= mini
            index += 1

        return answer
        #Time Complexity: O(1)
        #Space Complexity: O(1)