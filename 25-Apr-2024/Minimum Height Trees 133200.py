# Problem: Minimum Height Trees - https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        '''Approach: Topological Sort. The problem asks given a list of edges
        choose a node to be the root of a tree so that the tree can have minimum
        height. The basic intution behind this problem we want to minimize
        the height of a tree therefore nodes which have only one edge shouldn't
        be a root because they will definitely not give us the minimum height.
        A node to be a root it needs to contain more edges than other nodes
        in the tree. So nodes that have only one edge are considered to be
        leaf node. And it's obvious we can't make the leaf node a root. But
        we can start from all the leaf nodes and try going to the middle.
        In that case we can find the middle element but when do we know how
        to terminate because other than that it's basic topological sort. A
        graph can have a maximum of two possible roots when the minimum height
        is even otherwise it can only have one root. Therefore while performing
        toplogical sort we can check if we have reached the middle by checking
        if there are only two nodes remaining or less and return them.'''

        #if we have only one node then there is no edge that means the root is itself
        if n == 1:
            return [0]
        
        #build the graph and count the in degree to perform topological sort
        graph = defaultdict(list)
        in_degree = [0 for _ in range(n)]
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
            in_degree[node1] += 1
            in_degree[node2] += 1
        
        #find leave nodes and add them to the queue
        leaves = deque()
        for node, degree in enumerate(in_degree):
            if degree == 1:
                leaves.append(node)
        
        #perform topological sort using kahn's algorithm
        while leaves:

            #our termination point is if the number of nodes is less than or equal to 2
            if n <= 2:
                return list(leaves)
            
            #we need to iterate level wise because we are trying to reach the middle starting from all the leave nodes
            length = len(leaves)
            for _ in range(length):
                node = leaves.popleft()
                n -= 1 #decrement the number of nodes by 1
                for neighbour in graph[node]:
                    in_degree[neighbour] -= 1
                    #if a node become a leave node then add it to the queue
                    if in_degree[neighbour] == 1: 
                        leaves.append(neighbour)
        return []
        #Time Compelxity: O(V+2E) for performing BFS
        #Space Compelxity: O(V) for holding the queue
            
