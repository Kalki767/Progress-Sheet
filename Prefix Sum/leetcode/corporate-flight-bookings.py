class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        #Approach: prefix sum with range of queries
        '''Step1: create a list of prefix sum and populate it with zero that
        will be updated with each query'''
        prefix_sum = [0]*(n+1)

        '''Step2: iterate through each bookings and update their corresponding
        range of flight in the prefix sum since the flight range are one
        indexed they need to be decremented by one'''
        for first,last,seats in bookings:
            prefix_sum[first-1]+=seats
            prefix_sum[last]-=seats
        
        '''Step3: after the bookings are done calculate the prefix sum for
        each flight'''
        for index in range(1,len(prefix_sum)):
            prefix_sum[index]+=prefix_sum[index-1]

        '''Step4: return the prefix sum but since the last element will 
        always be zero we discarded'''
        return prefix_sum[:-1]
        #Time Complexity:O(n)
        #Space Complexity:O(n)