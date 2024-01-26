class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_count = Counter(nums1) #counting occurences
        nums2_count = Counter(nums2)
        value = []
        for key in nums1_count:
            if key in nums2_count: #if the key exists in both then take the minimum ocurrence and multiply it by the key to create a list
                val = min(nums1_count[key],nums2_count[key])
                value.extend([key]*val) #extend the obtained list
        return value