class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        '''Approach: Sorting. find the largest element from the list since
        we are given a list with elements starting from one we know the
        largest element from our size. after finding the index of the largest
        element we flip it twice to put it to it's last position then we will
        worry about the rest of the elements by doing the same'''

        #Step1: initialize result array
        result = []
        n = len(arr)

        '''Step2: iterate through the array once while finding the index of
        the largest element from the unsorted list'''
        for index in range(n):
            largest_index = arr.index(n - index)

            '''Step3: if the current element is already on it's desired
            place don't flip anything'''
            if largest_index == n-1-index:
                continue

            elif largest_index == 0:
                '''Step4: if the current element is on the first list then we
            need to do only one flip'''
                arr = list(reversed(arr[:n - index])) + arr[n - index:]
                result.append(n - index)
            else:
                '''Step5: we need to reverse the first elements to get the
                current element to the first then we can flip it to put it
                back to it's position'''
                reversed_array = list(reversed(arr[:largest_index + 1])) + arr[largest_index+1:]
                arr = list(reversed(reversed_array[:n - index])) + arr[n - index :]
                result.extend([largest_index + 1, n - index])
        return result
        #Time Complexity: O(n**2)
        #Space Complexity: O(n)