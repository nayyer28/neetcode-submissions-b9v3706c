# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 55
        # 22 --> simple add and create new node with sum

        # 55
        # 69 --> add first two, put unit's in node and move on with carry

        # 55 --> add first two, put unit's in node and move on with carry
        #  8

        # 55 --> same as 1)
        #  4

        # 55 --> 
        # 72

        r = res = None
        carry = 0
        while carry or l1 or l2:
            if not r:
                r = res = ListNode()
            else:
                r.next= ListNode()
                r = r.next

            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            s = v1 + v2 + carry

   
            curr = s % 10
            carry = s // 10
            r.val = curr

            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
            
        return res
        
        

