# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        '''Approach: DFS or topological sorting. The problem asks to
        find safe states. A state is said to be safe if it's either a
        terminal node or if all of it's edges lead to a terminal noe. To
        check if a node is a safe state all we have to do is check if that
        node has finished proccessing. If so then we will add it to our answer.
        But how do we know if a node finishes being proccessed. First we need
        to check if all of it's paths lead to a terminal if we get one path
        that doesn't lead to a terminal we immediately return false if we
        finished proccesing this node without returning false then we return
        True. The only case where a path won't lead to terminal state is
        when there is a cycle. Therefore when we detect cycle we return 
        false to the caller. And since the graph might be disconnected we
        need to run dfs on multiple nodes. Since the output need to be sorted
        we need to sort the output. To solve it with topological sorting we
        need to count the indegrees of every node and start from them but first
        we need to reverse the direction of each edge of the graph.'''
        answer = []
        colors = [0] * len(graph) #to detect cycles
        def dfs(node):
            if colors[node] == 1: #if we have come to the same node in the same path it's cycle
                return False

            #otherwise assign the current node as being processed
            colors[node] = 1

            for neighbour in graph[node]:
                #check if that node has already finished processing or not

                if colors[neighbour] != 2: 
                    #if we detect a cycle in one of the childs return false immediately
                    
                    if dfs(neighbour) == False: 
                        return False

            #if the node finished processing add it to our answer and update the color           
            colors[node] = 2
            answer.append(node)
            return True
        
        #since the graph might be disconnected we might need to call dfs multiple times
        for node in range(len(graph)):
            if colors[node] == 0:
                dfs(node)

        answer.sort() #since the expected output is in ascending order sort it

        return answer
        #Time Complexity: O(V+E + nlogn) where v is number of vertices and n is number of elements in our answer
        #Space Complexity: O(2V) one for call stack and another for storing the answer