# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def helper(r:Optional[TreeNode], lvl):
            if not r:
                return
            
            if len(res) == lvl:
                res.append(r.val)

            helper(r.right, lvl+1)
            helper(r.left, lvl + 1)
            
        
        helper(root,0)
        return res