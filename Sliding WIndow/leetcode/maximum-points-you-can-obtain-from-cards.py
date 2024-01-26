class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        #Approach: Sliding Window with fixed size
        #Step1: assign two pointers one to the end and one to k
        left,right=k-1, len(cardPoints)-1
        max_score =score= sum(cardPoints[:k])

        #Step2:check if the right pointer and left pointer are already equal so no need to iterate
        if right==left:
            return max_score

        #Step3:iterate through the array until the left pointer is less than zero
        while  left>=0:

            #Step4: updating the current score by decrementing the left and incrementing the right and taking the maximum of those two
            score = score-cardPoints[left]+cardPoints[right]
            max_score = max(max_score,score)
            left-=1
            right-=1
        return max_score
        #Time Complexity:O(n)
        #Space Complaxity:O(1)