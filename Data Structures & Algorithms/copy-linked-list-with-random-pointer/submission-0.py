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
        copies = {}
        copy = None
        while head:
            if head in copies:
                c = copies[head]
            else:
                copy = c = Node(head.val)
                copies[head] = c
            # next pointer
            if not head.next:
                c.next = None
            elif head.next in copies: # already created via last iteration's else
                c.next = copies[head.next]
            else: # lazy create
                c.next = Node(head.next.val)
                copies[head.next] = c.next

            # random pointer
            if not head.random:
                c.random = None
            elif head.random in copies: # already created in some prev iteration
                c.random = copies[head.random]
            else: # lazy create
                c.random = Node(head.random.val)
                copies[head.random] = c.random
            head = head.next
        return copy