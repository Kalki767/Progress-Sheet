# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        '''Approach: Topological Sort. The problem asks to find the quieter perosn
        among all that have equal or greater money. This means for any node finding
        the least quiet person from himself and his ancestors since his ancestors
        have obviously more money. Therefore while doing topological sorting we
        can update the least quite person we have found so far. Therefore if
        a node has no ancestor or a person who has more money than him then 
        the least quite person would be the person himself.So we start by 
        making the person itself the least quite person itself and while doing
        toplogical sort in which case we start from persons who doesn't have
        superiors we update it. We used the bfs traversal method for doing
        the topological sort. How can we update the list quiet person? We
        can carry the least quite person we have found till now in our in degree
        array and update  it whenever neccesary.'''
        
        #for bulding the graph given the edges
        length = len(quiet)
        graph = [[] for _ in range(length)]
        in_degree = [[0,i] for i in range(length)] #make the least quite person the person itself
        answer = [i for i in range(length)]
        queue = deque()

        #build the graph and update the in degree
        for rich, poor in richer:
            graph[rich].append(poor)
            in_degree[poor][0] += 1
        
        #if the current degree is zero this means it doesn't have any ancestor so add it to the queue
        for index, (degree,prev) in enumerate(in_degree):
            if degree == 0:
                queue.append((index,prev))
        
        #while there is an element in the queue keep iterating
        while queue:
            #pop the leftmost element
            index, quiet_index = queue.popleft()

            answer[index] = quiet_index #update the answer at the current index

            #iterate through it's neighbours
            for neighbour in graph[index]:

                in_degree[neighbour][0] -= 1
                prev_index = in_degree[neighbour][1] #previous least quiet person

                #check if we have found more quieter person
                if quiet[answer[prev_index]] > quiet[quiet_index]:
                    in_degree[neighbour][1] = quiet_index
                
                #if the current person has no more ancestors add it to the queue
                if in_degree[neighbour][0] == 0:
                    queue.append((neighbour,in_degree[neighbour][1]))

        return answer
        #Time Complexity: O(V+E) since it's normal bfs algorithm 
        #Space Complexity: O(V + E) for the in degree and for building the graph


