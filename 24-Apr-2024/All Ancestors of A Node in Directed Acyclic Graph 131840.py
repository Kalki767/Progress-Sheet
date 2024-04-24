# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        '''Approach: Topological Sort. The problem asks to find each and every
        ancestor of a node in a sorted manner. If a node doesn't have any ancestor
        then it we will just return an empty list. So how can we do that? One
        thing we need to know is it's talking abt ancestors and not parents
        therefore the grand parents of a node are it's ancestors too. Therefore
        reaching at any node we need to include the ancestors of that node and
        that node itself. So we can start with nodes that doesn't have any
        ancestor and as we move forward we add the current nodes and the
        ancestors of those nodes to our current node. But the problem arises
        when we arrive at a node which has the same ancestor but came from
        two different paths in that case we need to use a set not to repeat
        the same ancestors in our answer. Since the output is expected to
        be a sorted list we need to convert the set into list at last.'''

        #build the graph and count the in degrees for every node
        graph = [[] for _ in range(n)]
        in_degree = [0 for _ in range(n)]
        for start, end in edges:
            graph[start].append(end)
            in_degree[end] += 1
        
        #perform bfs traversal for topological sort
        queue = deque()
        answer = defaultdict(set)

        #start with nodes that doesn't have ancestor
        for index, degree in enumerate(in_degree):
            if degree == 0:
                queue.append(index)
        
        #while iterating through all the nodes update our answer
        while queue:
            index = queue.popleft()
            temp = [index]
            for neighbour in graph[index]:
                in_degree[neighbour] -= 1
                
                #the current node is an ancestor for it's child
                answer[neighbour].add(index) 

                #add the ancestors of the parent to the child node
                for val in answer[index]:
                    answer[neighbour].add(val)
                
                #if the child has no more direct parents add it to the queue
                if in_degree[neighbour] == 0:
                    queue.append(neighbour)

        #change the dictionary into a list
        result = [[] for _ in range(n)]
        for key,val in answer.items():
            result[key] = (list(sorted(val)))

        return result
        #Time Complexity: O(V+E + nlogn) where n is the size of the ancestor of each node
        #Space Complexity: O(n.k) where k is the size of the ancestor of each node