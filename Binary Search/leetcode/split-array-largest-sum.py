class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        '''Approach: Binary Search. The problem asks to find the minimum sum
        that we could acheive if we divide the array in to k parts. The split
        must be contigious. The approach we used is trying each and every sum
        that we could have and checking if having that sum perfectly splits
        the array into k parts if it does we update our sum and shrink the
        second half and decrease our sum if not we will check if the partition
        is too small or too big and we shrink one of the two halfs. If our 
        partition is less than k then our sum is big and we have to decrement
        it otherwise we have to increment it.'''
        lower_bound , upper_bound = max(nums), sum(nums)
        minimum_sum = float('inf')

        #for searching our maximum sum
        while lower_bound <= upper_bound:
            mid = lower_bound + (upper_bound - lower_bound)//2
            total = 0
            counter = 1
            for num in nums: #for counting the splits
                total += num
                if total > mid:
                    counter += 1
                    total = num
            if counter < k: #shrinking one of the two halfs
                upper_bound = mid - 1
            elif counter > k:
                lower_bound = mid + 1
            else:
                minimum_sum = min(minimum_sum,mid)
                upper_bound = mid - 1
        
        return minimum_sum if minimum_sum!=float('inf') else max(nums)
        #Time Complexity: O(nlogn)
        #Space Complexity: O(1)
