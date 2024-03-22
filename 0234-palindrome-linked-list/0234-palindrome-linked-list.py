# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        # Make a reversed copy, then make sure they're the same
        
        if head == None:
            return True
        
        temp = ListNode(head.val)
        original = ListNode(head.val, head.next);
        copy = head.next
        
        while head != None:
            copy = ListNode(head.val, copy)
            head = head.next
        
        while original != None:
            if original.val != copy.val:
                return False
            
            original = original.next
            copy = copy.next
        
        return True