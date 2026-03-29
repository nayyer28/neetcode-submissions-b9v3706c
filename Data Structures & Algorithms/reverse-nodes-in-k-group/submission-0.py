# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
            h = head
            k2 = k
            while h:
                h = h.next
                k2 -= 1
                if k2 == 0:
                    break
            if k2 > 0:
                return head

            i = 0
            tail = head
            prev = None
            while head:
                if i == k:
                    tail.next = self.reverseKGroup(head,k)
                    break
                nxt = head.next
                head.next = prev
                prev = head
                head = nxt
                i += 1
            
            return prev



