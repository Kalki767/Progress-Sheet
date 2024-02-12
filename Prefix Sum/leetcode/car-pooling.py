class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        '''Approach: prefix sum with range of queries. here we are given
        the start and end point of one travel therefore there would be that
        much number of passengers in that range and we decrease the number
        of passengers at their departure. so we used prefix sum to update
        number of passengers for range of values and calculate the prefix
        sum to know the total number of passengers that are in the bus at 
        the moment'''
        '''Step1: assign prefix sum list to 0 since at first the bus is carrying
        no passengers we can find the total number of bus stops by calculating
        the last departure from the trip'''
        last_departure = max([departure for num,start,departure in trips])
        passengers = [0]*(last_departure+1)

        '''Step2:update the number of passengers for each trip by updating
        the starting and the ending point'''
        for passenger,start,end in trips:
            passengers[start]+=passenger
            passengers[end]-=passenger
        
        '''Step3:calculate the prefix sum of passengers to know the total number
        of passengers at the current point'''
        for index in range(1,last_departure+1):
            passengers[index]+=passengers[index-1]
        
        '''Step4: find the maximum amount of passengers there were during the
        trip and if that number is greater than the capacity then return
        false otherwise return true'''
        max_passengers = max(passengers)
        if max_passengers>capacity:
            return False
        return True
        #Time Complexity:O(n)
        #Space Complexity:O(n)