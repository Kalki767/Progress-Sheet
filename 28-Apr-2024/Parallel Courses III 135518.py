# Problem: Parallel Courses III - https://leetcode.com/problems/parallel-courses-iii/

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        '''Approach: Toplogical Sort. The problem asks to find the minimum
        months it would take to finish all the courses which has one has
        dependency on another. The first thing that came to our mind is if
        we know which courses we can take at a moment then we can take the
        maximum at each stage but that's not true when we are taking the 
        maximum there are courses which finishes earlier therefore some other
        courses become available we can take that means we can reduce the
        time taken for those courses so that we would get the minimum amount
        of months.. The other reason is one course can have multiple prerequistes
        that means we have different paths to reach one node therefore the time
        it take to reach that course is the maximum of all those. Therefore
        what we can do is first take the courses with no prerequisites first
        and update their finishing time to be the time they took to finish.
        After that since those courses are finished update their child courses
        and their finishing time by taking the maximum one at last we will 
        return the maximum of all the finishing times. So the reason we used
        toplogical sort is because there is dependecy between them.'''

        #Step1: Build the graph and count the in degrees
        graph = [[] for _ in range(n+1)]
        in_degree = [0]*n

        #Step2: build the finishing time for each course at first that would be zero
        maximum_wait_time = 0
        wait_time = [0]*(n)
        queue = deque()

        for pre, course in relations:
            graph[pre].append(course)
            in_degree[course-1] += 1
        
        for index, degree in enumerate(in_degree):
            #take the courses which doesn't have any prerequsite and the maximum wait time would be the maximum of those
            if degree == 0:
                queue.append(index+1)
                wait_time[index] = time[index]
                maximum_wait_time = max(maximum_wait_time,wait_time[index])
        
        #Step3: perform kahn's algorithm for toposort
        while queue:
            course = queue.popleft()

            for pre in graph[course]:
                #update the current wait time to be the maximum of what it has or the parent plus it's time taken
                wait_time[pre-1] = max(wait_time[course-1]+time[pre-1],wait_time[pre-1])
                maximum_wait_time = max(maximum_wait_time,wait_time[pre-1])
                in_degree[pre-1] -= 1

                #if the current course doesn't have any prerequsites add it to the queue
                if in_degree[pre-1] == 0:
                    queue.append(pre)
        
        return maximum_wait_time
        #Time Complexity: O(n+e) for normal bfs traversal
        #Space Complexity: O(n) for queue, in degree, and for the wait time
