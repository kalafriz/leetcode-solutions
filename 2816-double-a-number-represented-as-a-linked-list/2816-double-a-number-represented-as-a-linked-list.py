# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: ListNode) -> ListNode:
        # If the value of the head node is greater than 4, 
        # insert a new node at the beginning
        if head.val > 4:
            head = ListNode(0, head)
        
        # Traverse the linked list
        node = head
        while node:
            # Double the value of the current node 
            # and update it with the units digit
            node.val = (node.val * 2) % 10
            
            # If the current node has a next node 
            # and the next node's value is greater than 4,
            # increment the current node's value to handle carry
            if node.next and node.next.val > 4:
                node.val += 1
            
            # Move to the next node
            node = node.next
        
        return head