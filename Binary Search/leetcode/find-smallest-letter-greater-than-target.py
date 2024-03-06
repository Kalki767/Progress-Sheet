class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        '''Approach: Binary Search. The problem asks to find the next smallest
        element fro the given list of letters. To find that we can simply use
        binary search and when we find an element which is greater than our 
        target letter we update our mid otherwise we keep looking.'''
        best = -1
        left, right = 0, len(letters)-1
        while left <= right:
            mid = left + (right - left)//2
            if letters[mid] <= target:
                left = mid + 1
            else:
                best = mid
                right = mid - 1
        if best == -1 :
            return letters[0]
        else:
            return letters[best]
        #Time Complexity: O(logn)
        #Space Complexity: O(1)
