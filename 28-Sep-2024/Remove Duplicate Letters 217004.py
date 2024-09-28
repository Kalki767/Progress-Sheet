# Problem: Remove Duplicate Letters - https://leetcode.com/problems/remove-duplicate-letters/

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        '''Approach: Monotonic Stack. The problem asks to find the smallest sequence
        that doesn't have duplicates. To solve this a basic observation would be that
        in the final answer it would be in increasing order but with one restriction
        all elements must be present which might fail the condition being increasing.
        For that case to include all of the unique letters we need to count the
        frequency of each element and track it as we traverse through it. Now when
        an element comes we check if it's already been in our result array that we
        are carrying if so we don't need to bother as we have already included it.
        If not we need to check the last element in our result and if this element
        is greater than the current element and it's frequency is greater than zero
        that mean we can remove this element because we can again find it in the future
        it's like swapping those two in the final answer to find the lexicographically
        smallest one. Finally we will simply return what's in our stack. For checking
        if the current element is already in our result or not we can use set for
        efficient lookup.'''
        stack = []
        visited = set()
        frequency = Counter(s)

        #iterate through the string
        for i in range(len(s)):

            #if the current element is not in our stack
            if s[i] not in visited:
                #check the condition to swap the two elements
                while stack and stack[-1] > s[i] and frequency[stack[-1]] > 0:
                    cur = stack.pop()
                    visited.discard(cur)
                #add the current element to our result
                visited.add(s[i])
                stack.append(s[i])
            frequency[s[i]] -= 1

        return "".join(stack)
        #Time Complexity: O(2n) where n is the length of the string
        #Space Complexity: O(m) where m is the unique letters in the string