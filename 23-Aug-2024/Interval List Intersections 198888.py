# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        #Step1: assign two pointers to the begining of the list and an empty list
        left=right=0
        ans = []

        #Step2: iterate through the list until one of them is exahusted

        while left<len(firstList) and right<len(secondList):

            #Step3: inpack the x and y variables from them

            first_x,first_y = firstList[left][0],firstList[left][1]
            second_x,second_y = secondList[right][0],secondList[right][1]

            #Step4: update x_at and y_at as the maximum and minimum of the unpacked tuples respectively

            x_at = max(first_x,second_x)
            y_at = min(first_y,second_y)

            #Step5: check if x_at>y_at and move the pointer to the right

            if x_at>y_at:
                if x_at==first_x:
                    right+=1
                else:
                    left+=1

            #Step6: if x_at is less than y_at check which variable y_at takes and update the pointer

            else:
                if y_at==second_y:
                    right+=1
                else:
                    left+=1

                #Step7: append x_at and y_at to our answer list

                ans.append([x_at,y_at])
        return ans
        #Time Complexity:O(n)
        #Space Complexity:O(1)
        