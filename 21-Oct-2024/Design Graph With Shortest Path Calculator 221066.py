# Problem: Design Graph With Shortest Path Calculator - https://leetcode.com/problems/design-graph-with-shortest-path-calculator/

class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        '''Approach: Dijkstra Algorithm. The problem asks to find the shortest path
        between two given nodes if there is a path between them if not we will simply
        return -1. This problem is asking to find the shortest path between some
        starting node and ending node. To solve this problem we first need to build
        our graph and the distance between any two nodes using matrix so that it
        would be easy to update the distance between them. After building the graph
        we need to make the distance between a node and itself as 0 and also while
        building the graph update the distance between the two nodes to be the weight.
        So whenever the shortest path between two nodes is asked we will traverse
        from the starting node and update the distances accordingly. After that we
        will return the distance if there is a path otherwise we will return -1.'''
        self.distances = [[float('inf') for _ in range(n)] for _ in range(n)]
        for i in range(n):
            self.distances[i][i] = 0
        self.graph = [[] for _ in range(n)]
        for start, end, cost in edges:
            self.distances[start][end] = cost
            self.graph[start].append([end,cost])

    def addEdge(self, edge: List[int]) -> None:
        start, end, cost = edge
        self.distances[start][end] = cost
        self.graph[start].append([end,cost])

    def shortestPath(self, node1: int, node2: int) -> int:
        heap = [(0,node1)]
        processed = set()
        while heap:
            dist, node = heappop(heap)
            if node in processed:
                continue
            processed.add(node)
            for child, cost in self.graph[node]:
                cur_dist = dist + cost
                if cur_dist <= self.distances[node1][child]:
                    self.distances[node1][child] = cur_dist
                    heappush(heap,(cur_dist,child))
        
        return self.distances[node1][node2] if self.distances[node1][node2] != float('inf') else -1
        #Time Complexity: O(V+E * log(V)) where V is the number of nodes given and E is edges
        #Space Complexity: O(V)


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)