class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        #Approach: Sliding Window
        #Step1: assign two pointers to the start of the array and minimum to infinity and windows dictionary to keep track of the occurrence of each element
        left=right=0
        min_cards = float('inf')
        windows = defaultdict(int)
        #Step2: iterate through the array while updating it's value in the window
        while right<len(cards):
            value = False
            windows[cards[right]]+=1

            #Step3: check if the occurrence of that element is greater than 1 and shrink the window size until we get unique elements

            while windows[cards[right]]>1:
                value = True
                windows[cards[left]]-=1
                left+=1

            #Step4: check if we have found duplicates and update the minimum
            if value==True:
                min_cards = min(min_cards,right-left+2)
            right+=1
        #Step5: check if the minimum value have been updated and return it or return -1
        if min_cards==float('inf'):
            return -1
        return min_cards 