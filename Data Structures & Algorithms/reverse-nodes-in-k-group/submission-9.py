# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # iteration - own approach with dummy node - optimistic reversal

        res = tail = ListNode()

        while True:
            # reverse
            org_head = head
            prev = None
            i = 0
            while head and i < k:
                nxt = head.next
                head.next = prev
                prev = head
                head = nxt
                i += 1
            # revert the reversal
            if i < k:
                head , prev = prev, head
                while head:
                    nxt = head.next
                    head.next = prev
                    prev = head
                    head = nxt
                tail.next = prev
                return res.next

            tail.next = prev
            tail = org_head
        



