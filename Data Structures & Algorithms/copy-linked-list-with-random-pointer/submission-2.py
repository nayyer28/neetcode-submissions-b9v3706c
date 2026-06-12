"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old2New = {None:None}

        copy = None
        h = head
        while head:
            if not copy:
                copy = Node(head.val)
                old2New[head] = copy
                res = copy
            else:
                copy.val = head.val
            
            # copy.next
            if head.next in old2New:
                copy.next = old2New[head.next]
            else:
                copy.next = Node(0)
                old2New[head.next] = copy.next

            # copy.random
            if head.random in old2New:
                copy.random = old2New[head.random]
            else:
                copy.random = Node(0)
                old2New[head.random] = copy.random
            
            head = head.next
            copy = copy.next
        
        return old2New[h]
            
            