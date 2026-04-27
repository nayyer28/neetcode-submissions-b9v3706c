# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        small, big = head, head
        i = 0
        while i < n:
            big = big.next
            i += 1
        
        if not big:
            return head.next
        
        while big.next:
            small = small.next
            big = big.next
        
        small.next = small.next.next
        

        return head

        
        
