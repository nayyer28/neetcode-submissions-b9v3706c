# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        small = big = head
        i = 0
        while i < n:
            big = big.next
            i += 1

        if not big: # corner case when first element must go
            return head.next
        
        while big and big.next:
            small = small.next
            big = big.next
        
        tmp = small.next
        small.next = tmp.next
        tmp.next = None

        return head