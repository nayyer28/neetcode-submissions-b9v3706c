# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #N<-0<-1<-2<-3 N
        #            p c

        p, c = None, head

        while c:
            nxt = c.next
            c.next = p
            p = c
            c = nxt
        
        return p