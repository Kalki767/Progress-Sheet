class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #Approach: Sliding Window with dynamic size
        
        '''Step1: assign the left pointer to the begining and a counter to 
        count the occurences of each element in our window'''
        left=max_length =0
        counter = defaultdict(int)

        #Step2:iterate through the list once and update the ocurrence of each character
        for right in range(len(s)):
            counter[s[right]]+=1

            '''Step3: since we want to maximize our length we need to find
            the most repeated element so that we should change the other values
            and not that chaarcter. so if the changes made to the characters
            that are not the most repeated is greater than k we need to shrink
            our window'''
            while (right-left+1)-max(counter.values())>k:
                counter[s[left]]-=1
                left+=1

            '''Step4: now the changes need to be made on the non frequent 
            characters is less than k so we can take our maximum length from
            the window'''
            max_length = max(max_length,right-left+1)
        return max_length
            