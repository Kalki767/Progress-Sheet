# Problem: Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''Approach: Min Heap. The problem asks to merge the given sorted linked
        lists. To do this we have multiple ways. One of the efficient way would
        be using a min_heap. Why do we use a min heap becuase it's efficient in
        both time and space complexity. How do we use min heap to our problem. The
        first element that our list is going to have is one of the first k
        elements of the list that means we only need to compare those value
        So what if we add those values into a heap therefore it would be easy
        to pop the minimum element. We can keep doing this retrieving the
        minimum element and adding new element to our heap until we are done
        iterating. But the problem arises the given list is linked list so
        when we are trying to add the node into the min heap it would create
        an error in python therefore for that purpose we need to hold the
        indexes and update the nodes whenever we are popping an element 
        because we want that index to point to the next element.'''
        min_heap = []

        #append the first k elements along with our index into our heap
        for index, node in enumerate(lists):
            #if the node is empty no need to append it to heap
            if node:
                heappush(min_heap, (node.val, index))
        
        dummy_node = ListNode() #create a node for holding the merged lists
        temp = dummy_node

        #do the sorting part until there are no elements in our heap
        while min_heap:

            value, index = heappop(min_heap)

            #assign the next minimum value to our originally sorted list
            temp.next = lists[index] 

             #update the current node to point to the next element
            lists[index] = lists[index].next

            #if we still have elements associated with this index
            if lists[index]: 
                heappush(min_heap,(lists[index].val,index))
            temp = temp.next #update the node to point to the next element

        return dummy_node.next
        #Time Complexity: O(nlogk) where n is total number of elements and k is number of lists
        #Space Complexity: O(k) for the min_heap
