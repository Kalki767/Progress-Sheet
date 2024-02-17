class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''Approach: Sliding window with dynamic size. here we need to find
        a substring which contains every element of t. to do that we used
        a sliding window to track how many elements we have encountered so
        far using a hashmap. so first we check if the current element exists
        in the target if it does we check have we found all duplicates of
        that character in our window if so that means we have found one
        character which satisfies our condition and we don't have to check 
        for that character again. so when we find all elements that satisfy 
        our condition we take the minimum window and shrink our window to 
        the right'''

        #Step1: if the given string is empty no need to find it
        if t == "": return ""
        
        #Step2: count the occurence of each element in t
        target = Counter(t)
        window = defaultdict(int)

        '''Step3: we are going to find the length of the target amount of
        unique characters in our string while checking their occurence'''
        have, need = 0, len(target)
        left = 0
        result, result_length = [0,0], float('inf')

        '''Step4: iterate through the array while adding the current element
        to the window'''
        for right in range(len(s)):
            character = s[right]
            window[character] += 1

            '''Step5:if the current character exists in the target and we
            have found each occurence of that character meaning the 
            frequency of the character in our window and target is equal
            then we need to increment the amount of character which
            satisfied our condition so far by one'''
            if character in target and window[character] == target[character]:
                have += 1
            
            '''Step6: now while all elements in our window have satisfied
            the condition which is their frequency we need to update our
            substring if the length is minimum'''
            while have == need:
                if (right-left+1) < result_length:
                    result = [left,right]
                    result_length = right-left+1
                
                '''Step7: shrink the window and check if the removed character
                was in t and if the frequency of the removed character is
                less than the frequency of that character in t decrement
                the have variable by one because we have found one
                character which doesn't met the criteria''' 
                window[s[left]] -= 1
                if s[left] in target and window[s[left]] < target[s[left]]:
                    have -= 1
                left += 1
        
        #Step8: if the length was not updated then t is not found in s
        if result_length!=float('inf'):
            l,r = result
            return s[l:r+1]
        return ""
        #Time Complexity: O(n)
        #Space Complexity: O(n)