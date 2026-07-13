# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        

        def merge2(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

            res = p = ListNode()
            while l1 or l2:
                if ( l1 and l2 and l1.val < l2.val ) or ( l1 and not l2 ):
                    p.next = l1
                    l1 = l1.next
                else:
                    p.next = l2
                    l2 = l2.next
                p = p.next
            
            return res.next
        
        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i + 1 < len(lists) else None
                merged.append(merge2(l1, l2))
            lists = merged
        return lists[0] if lists else None
        

                