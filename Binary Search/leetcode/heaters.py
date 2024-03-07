class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        '''Approach: Binary Search. The problem asks to find the minimum
        radius that the heaters need to have so that they could cover all
        houses. To solve this problem we need to check for each radius if
        the houses are covered by that. The range of radius extends from 0
        to the maximum values which is either the distance between the first
        and last elements or the distance between the last heater and the
        first element or viceversa. To check if a radius can cover all houses
        we have a helper function that checks and return True if we cover all
        houses and false if we don't to check that we check if either the
        current house is the house where we put our heater or if the heater
        distance is less than the house and adding radius results in a distance
        greater than the house or if the heater minus the radius is less than
        the house that means that heater can cover that house. One thing we
        need to consider is this logic only works in sorted input therefore
        we need to sort both inputs and we used binary search on the input
        to decrease our time complexity since the range maybe large.'''
        heaters.sort()
        houses.sort()

        #function to check if the current heater can cover all houses
        def CanCover(radius):
            index = counter = left = 0
            while index < len(houses) and left < len(heaters):
                house = houses[index]
                if house == heaters[left]:
                    counter += 1
                    index += 1
                elif heaters[left] < house and heaters[left] + radius >= house:
                    counter += 1
                    index += 1
                elif heaters[left] > house and  heaters[left] - radius <= house:
                    counter +=1
                    index += 1
                else:
                    left += 1
               
            return counter == len(houses)

        #setting bounds for our binary search
        lower_bound , upper_bound = 0 , houses[-1] - houses[0]
        Best_radius = max(upper_bound,abs(heaters[-1]-houses[0]),abs(heaters[0] - houses[-1]))

        #performing binary search on range of radius and updating radius as needed
        while lower_bound <= upper_bound:
            mid = lower_bound + (upper_bound - lower_bound)//2
            if CanCover(mid):
                Best_radius = mid
                upper_bound = mid - 1
            else:
                lower_bound = mid + 1

        return Best_radius
        #Time Complexity: O(nlogn)
        #Space Complexity: O(1)

