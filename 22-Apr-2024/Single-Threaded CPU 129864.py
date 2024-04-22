# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        '''Approach: Heap. The problem asks to schedule tasks in a way that
        a cpu with small processing time will be served first. So to solve
        this problem first we have to identify which computers will be
        available at the current time t all the cpus whose starting
        time is less than the current time and that has not been processed yet.
        So How do we determine that to get the minimum starting time we need
        to sort the input but if we sort the input we will lose the index of
        each cpu therefore we created another array for storing the indexes
        along with other information so that the index won't be lost when we
        sort the tasks based on their starting time. After doing that since
        all elements whose starting time is less than or equal to the current
        time are available task we need to choose a task that would be proccesed
        currently which is a task that have less processing time. We need to
        do this at each time get a cpu which has less processing time and a
        good datastructure for this is a heap after getting the cpu with
        minimum processing time the current time would be updated into
        either the next time or the current time plus the processing time. In
        our heap when there is tie we use second comparator which is the index
        as given in the problem statement.'''
        tasks_tobe_sorted = []
        length = len(tasks)

        #creating another array so that we won't lost the indexes when sorting
        for index in range(length):
            start_time, process_time = tasks[index]
            tasks_tobe_sorted.append((start_time,process_time,index))
        tasks_tobe_sorted.sort()
        min_heap = []
        current_time = tasks_tobe_sorted[0][0]
        answer = []
        index = 0

        #iterate through the sorted tasks one by one
        while index < len(tasks_tobe_sorted):

            #add every task whose starting time is less or equal to the current time
            while index < len(tasks_tobe_sorted) and tasks_tobe_sorted[index][0] <= current_time:
                heappush(min_heap, (tasks_tobe_sorted[index][1],tasks_tobe_sorted[index][2],tasks_tobe_sorted[index][0]))
                index += 1
            
            #if our heap is not empty pop out the cpu that has the minimum processing time
            if min_heap:
                process_time, ind, start_time = heappop(min_heap)
                answer.append(ind)
                current_time += process_time
            
            #if our heap is empty then the current time will be the next starting time
            else:
                current_time = tasks_tobe_sorted[index][0]
            
        #if there are any remaining cpus add them one by one based on their processing time
        while min_heap:
            process_time, ind, start_time = heappop(min_heap)
            answer.append(ind)

        return answer
        #Time Complexity: O(nlogn) both for sorting and for using heap while iterating once
        #Space Complexity: O(n) for creating new array 
