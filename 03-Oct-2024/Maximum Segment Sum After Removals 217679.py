# Problem: Maximum Segment Sum After Removals - https://leetcode.com/problems/maximum-segment-sum-after-removals/description/

class UnionFind:
    def __init__(self, size):
        self.parents = {i: i for i in range(size)}
        self.segment = {}  # Stores segment sums
        self.maxSegmentSum = 0  # Tracks the maximum segment sum

    def findParent(self, u):
        if u == self.parents[u]:
            return u
        self.parents[u] = self.findParent(self.parents[u])  # Path compression
        return self.parents[u]

    def Union(self, u, v):
        parent_u = self.findParent(u)
        parent_v = self.findParent(v)
        if parent_u != parent_v:  # Only union if they are in different sets
            self.parents[parent_v] = parent_u
            # Update the segment sum of the union
            self.segment[parent_u] += self.segment[parent_v]
            # Remove the old segment
            del self.segment[parent_v]
            # Update the maximum segment sum
            self.maxSegmentSum = max(self.maxSegmentSum, self.segment[parent_u])

    def addSegment(self, index, value):
        self.segment[index] = value
        # Update the maximum segment sum when a new segment is added
        self.maxSegmentSum = max(self.maxSegmentSum, value)


class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        '''Approach: Union Find. The problem asks to find the maximum segment upon 
        removing one index at a time. To solve this problem we know that consecutive
        elements make up a segment and at the start we have one segment which contains
        all indexes. But when removing one element we might still end up having one
        segment or split the previous segment into two. This means upon splitiing we
        have two segments which means we have two connected components. So that means
        the final segment was found by merging multiple segments together at every step.
        For this case if we start building from the last index that was removed as it
        was the only one left we see that the indexes start to merge one by one. Two
        indexes can be merged if they are neighbours. Now what datastructure is suitable
        for merging two connected components? Union Find! So we wil start from the last
        element and upon merging we update the segment sum if no merging happens at
        the current state then this index will stand alone for a while having it's
        own value as segment sum. Calculating the maximum sum at each step will take
        time so for efficiency we can track the maximum sum and update it at every
        step by taking the maximum sum and the current segment sum getting updated.'''
        n = len(nums)
        answer = [0] * n
        union_find = UnionFind(n)
        previous = set()  # Track previously added segments
        
        # Traverse in reverse order except for the last removal
        for i in range(n - 1, 0, -1):
            cur = removeQueries[i]
            union_find.addSegment(cur, nums[cur])  # Initialize the segment sum for this element
            
            # Union with adjacent segments if they exist
            if (cur + 1) in previous:
                union_find.Union(cur, cur + 1)  # Union with the right neighbor
            if (cur - 1) in previous:
                union_find.Union(cur, cur - 1)  # Union with the left neighbor
            
            previous.add(cur)  # Mark current index as added
            answer[i - 1] = union_find.maxSegmentSum  # Store the current maximum segment sum

        return answer
        #Time Complexity: O(n)
        #Space Complexity: O(n) where n is the total number of elements in nums
