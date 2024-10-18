# Problem: Find the City With the Smallest Number of Neighbors at a Threshold Distance - https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        '''Approach: Shortest Path Floyd Warshall Algorithm. The problem asks to find
        the city with the smallest number of cities that are reachable and the distance
        need to be less than the threshold. To solve this problem first we need to
        calculate the minimum distance starting from each node to every other node.
        After that we will count the nodes that can be reached from the current node
        with a distance of at most the threshold. Now how can we find the shortest
        path between each node. There are multiple algorithms some of them being 
        Dijkstra, bellman and Floyd Warshall. If we decide to move on with either
        Dijkstra or Bellman since both algorithms calculate the shortest path from
        some source node to every other node we need to run a loop on every node
        to find the shortest distance for all of them. In this case we are moving
        with Floyd Warshall to avoid unneccessary work. Applying the algorithm
        directly to our problem we can find the shortest path between every node.
        Then we find the city that has the minimum number of reach and update our
        answer accordingly.'''

        #Step1: declare a distances matrix and update the distances using the edges
        distances = [[float('inf') for _ in range(n)] for _ in range(n)]
        for start, end, dist in edges:
            distances[start][end] = dist
            distances[end][start] = dist
        
        #Step2: Apply floyd warshall algorithm to find the shortest paths
        for middle in range(n):
            for start in range(n):
                for end in range(n):
                    distances[start][end] = min(distances[start][middle]+distances[middle][end],distances[start][end])
        
        #Step3: Calculate the number of cities that can be reached with distance atmost threshold
        reachable = [0 for _ in range(n)]
        for start in range(n):
            for end in range(n):
                if start != end and distances[start][end] <= distanceThreshold:
                    reachable[start] += 1
        
        #Step4: Find the minimum distance and update the city with the minimum reachable accordingly
        mini = min(reachable)
        answer = -1
        for node in range(n):
            if reachable[node] == mini:
                answer = node

        return answer
        #Time Complexity: O(n**3)
        #Space Complexity: O(n**2) where n is the number of cities