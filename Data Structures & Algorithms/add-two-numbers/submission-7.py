# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = out = None
        s = 0
        while l1 or l2 or s:
            if l1:
                s += l1.val
                l1 = l1.next
            if l2:
                s += l2.val
                l2 = l2.next 
            if not curr:
                curr = out = ListNode(0)
            else:
                curr.next = ListNode(0)
                curr = curr.next
            curr.val = s % 10
            s = s // 10
        
        return out