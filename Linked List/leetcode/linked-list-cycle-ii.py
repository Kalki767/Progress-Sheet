# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Approach: Floyd cyle detection algorithm
        #Step1: first determine whether the list has cycle or not
        tortoise = rabbit = head
        while rabbit and rabbit.next:
            rabbit = rabbit.next.next
            tortoise = tortoise.next
            if rabbit == tortoise:
                break
        
        #Step2:check if we have detected a cycle or not
        if not rabbit or not rabbit.next:
            return None
        
        '''Step3: if there is a cycle since we already have found an
         intersection point we can restart our totroise at the head and move
         the rabbit and tortoise towards each other and count their moves
         until they are equal'''
        tortoise = head
        while tortoise != rabbit:
            tortoise = tortoise.next
            rabbit = rabbit.next
        return tortoise
        #Time Complexity:O(n)
        #Space Complexity:O(1)
        