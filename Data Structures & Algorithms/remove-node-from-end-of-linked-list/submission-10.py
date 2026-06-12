# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n == 0:
            return head
        
        fast = head
        i = 0
        while i < n and fast:
            fast = fast.next
            i += 1
        
        if not fast: # remove first
            head = head.next
            return head

        slow = head
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
    
        return head