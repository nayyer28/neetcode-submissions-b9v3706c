# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #   r
        #   1 2 3 4 5 6
        #         p h
        # 3 -> 2 -> 1
        # 6 -> 5 -> 4


        if not head:
            return None


        # can we reverse?

        h = head
        i = 0
        while h and i < k:
            h = h.next
            i += 1
        
        if i < k:
            return head
        
        prev = None
        org_head = head
        i = 0
        while i < k and head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
            i += 1
        # prev needs head of next reversal

        org_head.next = self.reverseKGroup(head, k)

        return prev

        
        