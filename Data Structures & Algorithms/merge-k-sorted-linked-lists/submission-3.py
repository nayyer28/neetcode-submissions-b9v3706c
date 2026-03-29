# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge2(l1:Optional[ListNode], l2:Optional[ListNode]):
            head = node = ListNode()
            while l1 or l2:
                if l1 and l2:
                    if l1.val < l2.val:
                        node.next = l1
                        l1 = l1.next
                    else:
                        node.next = l2
                        l2 = l2.next
                elif l1:
                    node.next = l1
                    l1 = l1.next
                else:
                    node.next = l2
                    l2 =  l2.next
                node = node.next
            return head.next
        
        if not lists:
            return None
        
        # L0, L1, L2, L3, L4, L5, L6, L7, L8
        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                merged.append(merge2(l1,l2))
            lists = merged
        return lists[0]
        

        


            
        
                
        