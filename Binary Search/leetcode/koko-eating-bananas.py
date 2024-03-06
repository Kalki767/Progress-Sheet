class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''Approach: Binary Search. The problem asks to find the minimum 
        number of bananas the girl need to eat in one hour so that she finishes
        up eating them when the guards came in. So the girl can eat one banana
        at the minimum and the maximum bananas that she could eat is the
        maximum of piles. Therefore we should perform a binary search on the
        piles and find a minimum number of bananas she need to eat in one hour
        so that she would finish eating them all. If the hours it would take
        her with the current speed is greater than the given hours she need to
        eat more bananas in an hour otherwise she can decrement the amount of 
        bananas she would eat in an hour.'''
        #for calculating the hour if she eats at the given speed
        def EatBanana(speed):
            hours = 0
            for index in range(len(piles)):
                if piles[index] <= speed:
                    hours += 1
                else:
                    if piles[index]%speed!=0:
                        hours += 1
                    hours += (piles[index]//speed)
            return hours
        lower_bound, upper_bound = 1, max(piles)
        Best_speed = upper_bound

        #for finding the minimum amount of bananas that she need to eat 
        while lower_bound <= upper_bound:
            mid = lower_bound + (upper_bound - lower_bound)//2
            hours_taken = EatBanana(mid)
            if hours_taken > h:
                lower_bound = mid + 1
            else:
                upper_bound = mid - 1
                Best_speed = min(Best_speed, mid)

        return Best_speed
        #Time Complexity: O(nlogn)
        #Space Complexity: O(1)