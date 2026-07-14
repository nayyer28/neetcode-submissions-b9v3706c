# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # iteration - own approach with dummy node - optimistic reversal

        def reverse(h:Optional[ListNode])-> (Optional[ListNode], Optional[ListNode], int):
            p = None
            i = 0
            while h and i < k:
                n = h.next
                h.next = p
                p = h
                h = n
                i += 1
            return (p,h,i)

        res = tail = ListNode()

        while head:
            # reverse
            org_head = head
            (nxtHead, head , i) = reverse(head)
            # revert the reversal
            if i < k:
                (nxtHead, _, _ ) = reverse(nxtHead)
                tail.next = nxtHead

            tail.next = nxtHead
            tail = org_head
        
        return res.next
        



