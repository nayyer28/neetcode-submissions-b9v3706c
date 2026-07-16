# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        q = deque([root])
        res = []
        while q:
            res.append([])
            # drain q entirely
            newq = []
            while q:
                nxt = q.popleft()
                res[-1].append(nxt.val)
                if nxt.left:
                    newq.append(nxt.left) 
                if nxt.right:
                    newq.append(nxt.right)
            q = deque(newq)
        return res
            






        
                
            
