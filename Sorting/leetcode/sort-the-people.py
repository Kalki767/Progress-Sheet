class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        for i in range(1,n):
            j =i
            value = heights[j]
            name = names[j]
            while j>0 and value>heights[j-1]: #comparing the current value with each and every sorted value which comes before it and finding it's correct position 
                heights[j] = heights[j-1]
                names[j] = names[j-1]
                j-=1
            heights[j] = value
            names[j] = name
        return names