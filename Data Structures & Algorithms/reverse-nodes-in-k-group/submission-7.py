# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # iteration - own approach with dummy node

        res = tail = ListNode()

        while True:
            # check if we have k left, else return
            h = head
            i = 0
            while h and i < k:
                h = h.next
                i += 1
            if i < k:
                tail.next = head
                return res.next

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

            tail.next = prev
            tail = org_head




