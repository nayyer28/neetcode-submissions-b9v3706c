"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        seen = {}
        def dfs(n:Optional['Node']) -> Optional['Node']:
            if not n:
                return None
            
            if n in seen:
                return seen[n]
            
            seen[n] = copy = Node(val=n.val)

            for neigh in n.neighbors:
                copy.neighbors.append(dfs(neigh))
            
            return copy
        
        return dfs(node)

