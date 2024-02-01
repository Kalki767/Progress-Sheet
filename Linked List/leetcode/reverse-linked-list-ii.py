# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        '''Approach: traverse through the linked list and reverse the given
        window and keep the other nodes in contact we will have two cases
        one when the left is 1 which result in updating the head and the
        other one is when the left is different from one which we can return
        the head itself'''
        distance = right-left+1
        #Step1: case1 when the left is greater than 1
        if left>1:

            '''Step2: since our left is different from the head we will always
            have a node before the left we will use that to connect it with
            our right node after reversal so we traverse through the linked
            list starting from the head until the left-1-1 since we need the
            element before the left our iteration should be left-1 and since
            we have 1 indexed variable we should decrement another 1 too'''
            Before_left_node = head
            for _ in range(left-2):
                Before_left_node = Before_left_node.next
            left_node = Before_left_node.next

            '''Step3: since we need our left node later to connect it with
            node that becomes after the right node we cannot update it
            for the reversal part so we would assign another node to left
            node and a previous node for the reversal'''
            reverse_node = left_node
            previous_node = None
            while distance>0:
                temp = reverse_node.next
                reverse_node.next = previous_node
                previous_node = reverse_node
                reverse_node = temp
                distance-=1
            
            '''Step4: now we need to connect our remainig before left node
            and after right node with their respective values after the
            reversal'''
            after_right_node = temp
            right_node = previous_node
            Before_left_node.next = right_node
            left_node.next = after_right_node
        #Step5: if our left is equal to one
        else:

            '''Step6: here since the left is one our left node will be equal
            to the head and our right node can be found while reversing after
            the reversal our head will be updated to the right node and the 
            left node should imply to the node that comes after the right node
            '''
            reverse_node = left_node = head
            previous_node = None
            while distance>0:
                temp = reverse_node.next
                reverse_node.next = previous_node
                previous_node = reverse_node
                reverse_node = temp
                distance-=1
            head = previous_node
            left_node.next = reverse_node
        return head

