# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:       
        if not list1:
            return list2
        if not list2:
            return list1
        # 1 3 4 
        # 2 5
        # 1 2 3 4 5
        if list1.val < list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
        c = head
        while c:
            if not list1 and list2:
                c.next = list2
                list2 = list2.next
            elif not list2 and list1:
                c.next = list1
                list1 = list1.next
            elif not list1 and not list2:
                c.next = None
            elif list1.val < list2.val:
                c.next = list1
                list1 = list1.next
            else:
                c.next = list2
                list2 = list2.next
            c = c.next
        
        return head
            


        