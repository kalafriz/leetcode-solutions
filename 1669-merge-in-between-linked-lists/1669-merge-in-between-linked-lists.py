# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        result = ListNode(list1.val)
        head = result
        
        current = list1.next
        l1_iter = list1.next
        i = 1
        
        # SEGMENT 1: head -> a-1
        while current.next != None and i < a:
            result.next = ListNode(current.val)
            result = result.next
            current = current.next
            
            l1_iter = l1_iter.next
            i+=1
            
        # SEGMENT 2: Insert list2
        current = list2
        while current != None:
                
            result.next = ListNode(current.val)
            result = result.next
            current = current.next
            
        # SEGMENT 2b: Catch up list 1 iterator
        while i < b+1:
            l1_iter = l1_iter.next
            i+=1
            
        # SEGMENT 3: b+1 -> end
        current = l1_iter
        while current != None:
                
            result.next = ListNode(current.val)
            result = result.next
            current = current.next
            
        return head