# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 1 2 3 4 5 6
        def getKth(cur):
            k2 = k
            while cur and k2 > 0:
                cur = cur.next
                k2 -= 1
            return cur
        
        dummy = ListNode(0,head)
        prevGroupHead = dummy

        while True:
            kth = getKth(prevGroupHead)
            if not kth:
                break

            nextGroupHead = kth.next

            prev = kth.next
            cur = prevGroupHead.next

            while cur != nextGroupHead:

                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            
            tmp = prevGroupHead.next # old group's original head points to the old head of the next group or the new tail
            prevGroupHead.next = kth # attach prev group's original head/new tail to the new head of the next group
            prevGroupHead = tmp # move prevGroupHead to point to the new tail/old head of the next group
        
        return dummy.next # dummy.next goes from pointing to 1 to 3 via lines 36-37

        



        



