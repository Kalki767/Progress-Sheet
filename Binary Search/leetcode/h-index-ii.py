class Solution:
    def hIndex(self, citations: List[int]) -> int:
        '''Approach: Binary Search. The problem asks to find the maximum h
        value where the citation has at least h papers with citation of at
        least h. Therefore the minimum citation we could have is 1 and the
        maximum is the length of the citation because we need at least h
        papers. So we can just find the bisect left of current h and check
        if we have atleast h papers with citations of h the way we do that
        is by just checking if the remaining elements are greater than or equal
        to h if not we shrink the second half if we have we shrink the first 
        half and update our h. If the h hasn't been updated at all we will 
        simply return 0 if it has been updated we will return h.'''
        h = float('-inf')
        n = len(citations)
        lower_bound , upper_bound = 1,n
        while lower_bound <= upper_bound:
            mid = lower_bound + (upper_bound - lower_bound)//2
            index = bisect_left(citations,mid)
            if n - index >= mid:
                h = max(h,mid)
                lower_bound = mid + 1
            else:
                upper_bound = mid -1
        return h if h!= float('-inf') else 0
        #Time Complexity: O(lognlogn)
        #Space Complexity: O(1)