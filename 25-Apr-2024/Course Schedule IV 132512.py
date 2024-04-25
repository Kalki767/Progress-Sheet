# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        '''Approach: Topological Sorting Using Kahns Algorithm. The problem
        asks given the connection between the prerequiste and course we need
        to check if to courses have that connection for the given queries.
        So How can we do that? If we keep track of all the prerequistes to
        a course then we can succesfully check whether they have a connection
        or not in O(1) time complexity. But how do we do that. This problem is
        the same as with finding the ancestors of a node only in this case after 
        we have find the ancestors we need to answer queries based on the given
        ancestors. To build the ancestor we started with nodes who doesn't have
        any ancestor and as we move forward we update our ancestors. We have used
        set to avoid duplicate values.'''

        #first build the graph and count the in degree
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        for pre, course in prerequisites:
            graph[pre].append(course)
            in_degree[course] += 1
        
        #create a dictionary with default set for holding the ancestors
        result = defaultdict(set)

        #add the nodes which doesn't have any ancestors
        queue = deque()
        for key, val in graph.items():
            if in_degree[key] == 0:
                queue.append(key)
        
        #perform kahn's algorithm to find the ancestor of any node
        while queue:
            pre = queue.popleft()
            for course in graph[pre]:
                in_degree[course] -= 1
                result[course].add(pre) #the current node is the ancestor of it's child

                #the ancestor of the part are also the ancestor of the child
                for val in result[pre]:
                    result[course].add(val)
                
                #if we have finished finding all ancestors of a node then add it to our queue
                if in_degree[course] == 0:
                    queue.append(course)
        
        #update ur answer for range of queries
        answer = []
        for pre, course in queries:
            answer.append(pre in result[course])

        return answer
        #Time Complexity: O(V+E)
        #Space Complexity: O(V+E)
