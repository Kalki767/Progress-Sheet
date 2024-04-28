# Problem: Meeting Rooms III - https://leetcode.com/problems/meeting-rooms-iii/

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        '''Approach: Heap. The problem asks given set of rooms and meetings
        with their starting and ending time we need to find a room which has
        been used most frequent. We can schedule meetings starting from the
        smallest index. The approach that we used here whenever a new meeting
        comes in we need to check if there are any meetings that can left
        that means we check if there were any meetings that ended before the
        current start and we make those rooms free. That means we are going
        to add those rooms to our available rooms. And after doing that we
        simply check do we have available rooms if so then we will simply
        take the room with the smallest index and add that meeting otherwise
        the current meeting has to wait until one meeting leaves a room.
        Obviously the meeting with the smallest ending time will end first.
        When the current meeting is added we update the start and end time
        because it's been delayed. Since we are continuosly finding minimum
        values for finding an available room and for finding a meeting with
        the smallest ending we use heap for efficient retrieval. One thing
        we shouldn't forget is the input is not sorted so we need to sort
        it.'''
        #Step1: sort the meetings and declare an answer to hold the amount of meetings it had
        meetings.sort()
        answer = [0]*n
        heap = []

        # heapify the available rooms for efficient access
        available = [room for room in range(n)]
        heapify(available)

        #Step2: iterate through the meetings
        for index, (start, end) in enumerate(meetings):

            #if there are any meetings that ended before now or currently make the room free
            while heap and heap[0][0] <= start:
                prev_end, prev_index, prev_start = heappop(heap)
                answer[prev_index] += 1 #update the number of meetings for that room
                heappush(available,prev_index) #add that room to available rooms
            
            #if we have any available rooms then take the one with minimum index and add the meeting to the heap
            if available:
                room_number = heappop(available)
                heappush(heap, (end,room_number,start))
            
            #otherwise we need to wait until one meeting ends which results in delay
            else:
                prev_end, prev_index, prev_start = heappop(heap)
                delay = prev_end  - start #calculating the delay of time
                start = prev_end
                end = end + delay #postponing the end by the dealy
                answer[prev_index] += 1
                heappush(heap, (end , prev_index, start))

        #if there are any elements in the heap that have not yet been finished update their room numbers        
        while heap:
            prev_end, prev_index, prev_start = heappop(heap)
            answer[prev_index] += 1
        
        #Step3: find the room with maximum value and minimum index for that start traversing backward
        maximum = float('-inf')
        index = n - 1
        max_index = 0

        #iterate backwards so that we can find the maximum value correctly
        while index > -1:
            if answer[index] >= maximum:
                max_index = index
                maximum = answer[index]
            index -= 1 
        
        return max_index
        #Time Compelxity: O(nlogn) for sorting and performing heap operation inside a loop
        #Space Complexity: O(n) for holding available rooms and meetings 
        