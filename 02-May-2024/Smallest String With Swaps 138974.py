# Problem: Smallest String With Swaps - https://leetcode.com/problems/smallest-string-with-swaps/

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        '''Approach: Union Find. The problem asks given pairs of indexes to
        swap we need to return the lexicographically smallest string that
        we can acheive. Here the basic intuition behind the problem is we
        might be given multiple pairs of indexes to swap where there might
        be connection in the pairs that means from all the indexes that have
        a connection we need to find the first smallest and then the second
        smallest and so on. So we can see this problem as graph problem where
        we will have multiple connected components where we would have to
        sort the connected components. And which data structure is a good
        fit for determining connected components? Union Find. Therefore first
        starting from each pairs we are going to identify the connected compnents
        Then we need to sort the connected components but here for unioning
        two pairs we will be using the indexes for that reason we need to store
        the letters along with them therefore both should be sorted atlast.
        But in this code we used heap instead of sorting which is a somehow
        efficient than sorting but instead of adding the elements into
        a list and then sorting the whole thing since we are using a heap it
        will create a min heap in logn time and when we are building our
        index we will take out the elements in logn time.'''

        #Step1: define a function for finding a parent of node using path compression
        parents = {i:i for i in range(len(s))}
        def findParents(node):
            if node == parents[node]:
                return node
            parents[node] = findParents(parents[node])
            return parents[node]
        
        #Step2: define a function for unioning two nodes together
        def union_find(u,v):
            parent_u = findParents(u)
            parent_v = findParents(v)
            if parent_u == parent_v:
                return
            parents[parent_u] = parent_v
        
        #Step3: create two dictionaries one to hold the connected indexes and the other is for their corresponding letters
        result = defaultdict(list)
        mapping = defaultdict(list)

        #Step4: build our graph
        for u, v in pairs:
            union_find(u,v)
        
        #Step5: build the two dictionaries but use heap instead of regular list
        for key, value in parents.items():
            parent = findParents(key)
            heappush(result[parent],key)
            heappush(mapping[parent],s[key])
        
        #since python string is immutable use a list for updating characters
        answer = list(s)
        for key in mapping:

            #to find the minimum index and letter pop out from the heap
            first_heap = result[key]
            second_heap = mapping[key]
            while first_heap and second_heap:
                index = heappop(first_heap)
                character = heappop(second_heap)
                answer[index] = character
           
        return "".join(answer)
        #Time Complexity: O(nlogn) for performing heap operation inside a loop
        #Space Complexity: O(n) for storing the dictionaries 