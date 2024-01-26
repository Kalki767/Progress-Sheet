class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        #Approach: Sliding Window
        #Step1: assign two pointers to the start of the list and a default dictionary to store count of type of fruits
        left=right=0
        window = defaultdict(int)
        type_of_fruit=max_fruit=0

        #Step2: iterate through the array while adding the current element to the window
        while right<len(fruits):
            window[fruits[right]]+=1

            #Step3:check if the element has occured once and update the type of fruits in the window
            if window[fruits[right]]==1:
                type_of_fruit+=1
            
            #Step4: check if the type of fruit is greater than 2 and update the maximum fruit that can be obtained
            if type_of_fruit>2:
                max_fruit = max(max_fruit,right-left)
            
            #Step5: shrink window size until the type of fruits is down to 2
            while type_of_fruit>2:
                window[fruits[left]]-=1
                if window[fruits[left]]==0:
                    type_of_fruit-=1
                left+=1
            right+=1
        
        #Step6: take the maximum fruit outside the loop too
        max_fruit = max(max_fruit,right-left)
        return max_fruit
        #Time Complexity:O(n)
        #Space Complexity:O(n)