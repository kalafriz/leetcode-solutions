# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Make a reversed copy, then insert
        
        if head == None:
            return None
        
        copy = ListNode(head.val, head.next)
        rcopy = ListNode(head.val)
        temp = head.next
        n=1
        
        while temp != None:
            rcopy = ListNode(temp.val, rcopy)
            temp = temp.next
            n+=1
            
        i=0
        top = head
        copy = copy.next
        #print(copy)
        #print(rcopy)
        while i<n-1:
            #print("i=",i, " , copy,rcopy=",copy.val,rcopy.val)
            #print(top)
            if i%2 !=0:
                head.next = ListNode(copy.val)
                copy = copy.next
            else:
                head.next = ListNode(rcopy.val)
                rcopy = rcopy.next
            head = head.next
            i+=1
        
