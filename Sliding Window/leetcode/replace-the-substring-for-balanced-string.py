class Solution:
    def balancedString(self, s: str) -> int:
        #Approach: Sliding Window with dynaimc size
        '''Step1: calculate the number of occurences that need to be in the
        string and a dictionary to count the occurence of each element'''
        counter = Counter(s)
        target = len(s)//4
        min_length = float('inf')

        '''Step2: check if the string is already balanced we can do that by
        taking if the maximum value from our counter is greater than the
        target then our string is not balanced'''
        if max(counter.values())==target:
            return 0

        '''Step3: if the string is not balanced use a sliding window to
        check if the removal of the current window will make the string
        balanced'''
        left =0
        for right in range(len(s)):
            counter[s[right]]-=1
            
            '''Step4: if the maximum occurence in the counter is equal
            to the target update the min_length'''
            if max(counter.values())==target:
                min_length = min(min_length,right-left+1)

                '''Step5:shrink the window from the left and add the removed
                element and check if it's still balanced string if not break
                the loop'''
                while left<=right:
                    counter[s[left]]+=1
                    left+=1
                    if max(counter.values())==target:
                        min_length = min(min_length,right-left+1)
                    else:
                        break
        return min_length
        #Time Complexity:O(n)
        #Space Complexity:O(1)