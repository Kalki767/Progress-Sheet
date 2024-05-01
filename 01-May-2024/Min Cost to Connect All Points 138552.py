# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        '''Approach: Union Find. The problem asks to find the minimum cost
        to connect all points. So first we need to know the cost of connecting
        each point to one another so that we would take the minimum one. But
        sometimes there doesn't need to be a direct connection between two
        points. They might be connected indirectly if that is the minimum
        distance. So first let's build a graph which is an edge between two
        points and the cost of connecting them let's take that as weight of
        the graph. After that we need to sort based on the cost so that we
        will have the minimum costs first. Whenever we are making a connection
        we check that if this connection is necessary that means we need to
        check if these points have not already been connected before. And which
        algorithm does that in constant time that would be union find!! So
        after sorting the graph we will modify our union find algorithm a
        little bit by checking if they are already connected we don't need
        to do anything otherwise this connection is neccesary because since
        the graph is already sorted we won't be able to find a minimum cost
        after this point to connect those two points. That means we will add
        this cost to our answer.'''
        
        #Step1: build the graph along with the cost in which the cost is the manhatan distance
        graph = []
        answer = 0
        for i in range(len(points)):
            init_x, init_y = points[i]
            for j in range(i+1,len(points)):
                final_x, final_y = points[j]
                weight = abs(final_x - init_x) + abs(init_y - final_y)
                graph.append([i,j,weight])
        
        #Step2: sort the graph based on the cost to have the minimum costs at the top 
        graph.sort(key = lambda x: x[2])

        #Step3: initialize the parent for union find we will use the index for ease of use
        parents = {i:i for i in range(len(points))}
        rank = {i:0 for i in range(len(points))}
        
        #Step4: define a function to find the parent of a given node
        def findParents(node):
            if node == parents[node]:
                return node
            parents[node] = findParents(parents[node])
            return parents[node]
        
        #Step5: define the union find function with a simple modification to calculate the cost
        def union_find(u,v,w):
            nonlocal answer
            parent_u = findParents(u)
            parent_v = findParents(v)
            if parent_u == parent_v:
                return False
            
            #use union by rank for efficient merging of the two nodes
            if rank[parent_u] < rank[parent_v]:
                parents[parent_u] = parent_v
            elif rank[parent_v] < rank[parent_u]:
                parents[parent_v] = parent_u
            else:
                parents[parent_u] = parent_v
                rank[parent_v] += 1

            #if we end up merging the two nodes then that means this edge was necesary so add it's cost
            answer += w
            return True
        #Step6: iterate through the sorted graph and make the necessary connections
        for u, v, w in graph:
            union_find(u,v,w)
        return answer

        #Time Complexity: O(n**2) for building the graph
        #Space Complexity: O(n) for the graph the parent and the rank