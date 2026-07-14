# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # iterative - own try
        res = None
        tail = None
        while True:
            # check if you have k nodes left
            h = head
            i = 0
            while h and i < k:
                h = h.next
                i += 1
            if i < k:
                break
            
            prev = None
            org_head = head
            i = 0
            while head and i < k:
                nxt = head.next
                head.next = prev
                prev = head
                head = nxt
                i += 1
            
            if not res:
                res = prev
            
            if tail:
                tail.next = prev

            tail = org_head
            
            
        
        if tail:
            tail.next = head
        return res if res else head
            
        
        