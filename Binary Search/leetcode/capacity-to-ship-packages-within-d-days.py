class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        '''Approach: Binary Search. The problem asks to find the minimum
        weigth that the ship need to hold at a time so that we could carry
        all the packages within the given days. To find that the first thing
        we need to do is find the minimum and maximum capacity we need to 
        have so that we can carry all the packages. So the minimum capacity
        is the maximum of the packages and the maximum weight is the sum of
        all packages so that we can carry all packages in one day. Since we
        need optimized weight we are going to check for every weight in the
        range the total days it would take and if it take less than or equal
        to the given days we update our weight and try another weight value.
        we used a binary search for the weight to optimize it's value.'''

        def CountDays(weight):
            Current_weight = 0
            Days = 1
            for index in range(len(weights)):
                Current_weight += weights[index]
                if Current_weight > weight:
                    Days +=1
                    Current_weight = weights[index]
            return Days

        Best_weight = sum(weights)
        lower_bound, upper_bound = max(weights), sum(weights)
        
        #check for weight in the given range and update the weight
        while lower_bound <= upper_bound:
            mid = lower_bound + (upper_bound - lower_bound)//2
            Days_needed = CountDays(mid)
            if Days_needed > days:
                lower_bound = mid + 1
            else:
                upper_bound = mid -1
                Best_weight = min(Best_weight, mid)


        return Best_weight
        #Time Complexity: O(nlogn)
        #Space Complexity: O(1)
