# Problem: Longest Cycle in a Graph - https://leetcode.com/problems/longest-cycle-in-a-graph/

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        '''Approach: DFS with topological sort. The problem asks to return
        the maximum number of nodes in the longest cycle. To do that first we 
        need to find a node that is part of a cycle. And since one node can
        have at most one edge a node can be at most part of one cycle. So
        to detect the cycles we can use topological sort or simple dfs. But
        since the graph is directed we need to have three colors to detect
        cycle. Whenever we detect a cycle call some function to count the
        number of nodes associated with that cycle. And once we are done
        counting the nodes we take the maximum one.''' 
        n = len(edges)
        max_nodes , nodes = 0,0
        visited = set()
        colors = [0 for i in range(n)]

        #for counting the number of nodes in the given cycle
        def count_nodes(node):
            nonlocal max_nodes , nodes
            if node  in visited:
                return
            visited.add(node) #not to visit the same node twice since it's cycle
            nodes += 1

            #since each node has atmost one edge and in this case since it's cycle all nodes have one edge
            count_nodes(edges[node]) 

            #take the maximum one
            max_nodes = max(nodes,max_nodes)
            
        #perform normal dfs to find nodes which have cycle
        def topsort(node):
            nonlocal nodes
            #check if there is cycle and whenever there is cycle start the nodes from 0
            if colors[node] == 1:
                nodes = 0
                count_nodes(node)
                return
            colors[node] = 1 #mark the node as currently being proccesed

            #if the current node doesn't have any outgoing edge mark it as visited
            if edges[node] == -1:
                colors[node] = 2
                return
            
            '''if we have been to the current node before and we have 
            finished proccesing it then that means we have finished 
            proccesing the current node'''
            if colors[edges[node]] == 2:
                colors[node] = 2
                return

            #otherwise call the function recursively
            topsort(edges[node])
            colors[node] = 2

        #since the graph might be disconnected  we might need to run the dfs multiple times
        for i in range(n):
            if colors[i] == 0 and edges[i] != -1:
                topsort(i)
        
        return max_nodes if max_nodes else -1
        #Time Complexity: O(V+E)
        #Space Complexity: O(V) for color array
        