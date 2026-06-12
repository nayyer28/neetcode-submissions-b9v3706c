# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        

        # halfway point now in slow
        # reverse from slow to end

        p = None
        while slow:
            nxt = slow.next
            slow.next = p
            p = slow
            slow = nxt
        
        # now p holds the reversed linked list

        curr, tar = head, p

        while curr:
            nxt = curr.next
            curr.next = tar
            curr = tar
            tar = nxt

        

        