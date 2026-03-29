# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        l2 = slow.next
        prev = slow.next = None

        while l2:
            nxt = l2.next
            l2.next = prev
            prev = l2
            l2 = nxt
        
        a, c = head, prev

        while c: # second list is the smaller one
            b = a.next
            d = c.next
            a.next = c
            c.next = b
            a = b
            c = d