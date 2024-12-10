# Problem: Remove All Adjacent Duplicates in String II - https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/description/

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        '''Approach: Stack. The problem asks to delete any adjacent characters that
        are the same and have a length of k. To solve this problem a brute force 
        approach would be to delete every substring at each position and iterate
        until we can no longer delete a substring this method is inefficient because
        we are traversing through the string multiple times. To optimize this let's
        observe somethings. What are the things that we are doing repeatedly. Here
        we need to know if the frequency of consecutive characters is k so that we
        can remove them. For that we need to know the frequency of the previous one
        and once we have reached k we can remove the last k characters. What's the
        best data structure for removing from the end and adding on the end. Stack!
        While traversing through the string we can hold the frequency alongside
        with it and when the frequency reaches k we can pop out them. Finally what
        remains in the stack is our answer.'''
        stack = []

        for index, char in enumerate(s):
            if stack and stack[-1][0] == char:
                stack.append([char,stack[-1][1]+1])
            else:
                stack.append([char,1])
            if stack[-1][1] == k:
                for i in range(k):
                    stack.pop()

        if not stack:
            return ''

        ans = [i[0] for i in stack]
        return ''.join(ans)
        #Time Complexity: O(n)
        #Space Complexity: O(n)