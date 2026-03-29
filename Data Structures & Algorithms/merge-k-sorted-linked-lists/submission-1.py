# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists:
            return None

        for i in range(len(lists) - 1):
            l1 = lists[i]
            l2 = lists[i+1]
            node = head = ListNode()
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
            lists[i+1] = head.next
        
        return lists[-1]
        
                
        