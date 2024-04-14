# Problem: Sort List - https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''Approach: MergeSort. The problem asks to sort the given linked
        list. We can sort it in many ways but to fit into the time constraints
        we will use merge sort. Therefore to perform merge sort on it first
        we need to find the mid node to do that we will use fast and slow
        pointers after that to go to the left since it's a linked list and not
        an array we will set the next to be null after finding the mid node
        and for the right part we will start with mid.next. After finding 
        the left and right indexes we will merge them usingm two pointers
        and return the head of the merged lists.'''

        #to find the middle node of the linked list
        def find_mid(node):
            slow , fast = node, node.next
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            return slow
        
        #for dividing the linked list into 2 parts recursively
        def mergeSort(node):
            #if the current node is empty or doesn't have any next we just return the node
            if not node or not node.next:
                return node
            mid_node = find_mid(node) #find the middle node
            right = mid_node.next
            left = node
            mid_node.next = None
            left_node = mergeSort(left) #call the function to find the left half
            right_node = mergeSort(right) #call the function to find the right half

            return merge(left_node,right_node)
        
        #function to merge the two lists
        def merge(left_node,right_node):
            temp = dummy_node = ListNode() #create a dummy node for merging the two
            while left_node and right_node:
                if left_node.val <= right_node.val:
                    dummy_node.next = left_node
                    left_node = left_node.next
                else:
                    dummy_node.next = right_node
                    right_node = right_node.next
                dummy_node = dummy_node.next
            #if there are still elements left append them to the end
            if left_node:
                dummy_node.next = left_node
            if right_node:
                dummy_node.next = right_node
            return temp.next #since the dummy node doesn't contain any value
        result = mergeSort(head)
        return result
        #Time Complexity: O(nlogn)
        #Space Complexity: O(n)