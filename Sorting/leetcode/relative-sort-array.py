class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        #since each element of arr2 exists in arr1 we can use that as an advantage
        arr1_map = Counter(arr1) #counting ocurrences of each element
        arr1.clear()
        for i in arr2: #iterating through arr2
            arr1.extend([i]*arr1_map[i]) #for each element in arr2 append it to arr1 by multiplying it with its occurence
            del arr1_map[i] #removing that key
        values = []
        for key in arr1_map: #adding the remaining elements which are not a member of arr2
            values.extend([key]*arr1_map[key])
        values.sort()
        arr1.extend(values)
        return arr1
        # time complexity : O(n)
        # space complexity : O(n)