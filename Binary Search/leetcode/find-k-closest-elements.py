class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        '''Approach: Binary Search. The problem asks to find the k closest
        elements to the given value. if the value itself exists in the array then
        it's counted as one closest element. Therefore to solve the problem
        we used binary search but here we are searching for a window of size
        k not an individual element. Our condition is can we find a better
        window to the right we can do that by checking if the element next to
        the last element of the window is closer than the starting of the
        window then we should avoid the starting of the element in our window
        and add the element which is next to last if that is not the case
        we don't know if there is a better solution to the left so we gotta
        hold the current starting point we have therefore we will just shrink
        the right until the current mid because the current window might be
        the one that we could achieve at best. Finally the loop terminates
        when the left and right pointers are equal so after that we could return
        the elements in the window starting from the left pointer with size k.'''

        left , right = 0, len(arr) - k
        while left < right:
            mid = left + (right - left)//2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left:left+k]
        #Time Complexity: O(logn)
        #Space Complexity: O(1)