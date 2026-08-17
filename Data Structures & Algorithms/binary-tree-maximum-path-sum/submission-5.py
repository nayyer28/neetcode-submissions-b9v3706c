# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        mx = float("-inf")

        def dfs(r:Optional[TreeNode]) -> int :  # return gain
            nonlocal mx
            if not r:
                return 0
            
            lg, rg = max(0,dfs(r.left)), max(0,dfs(r.right))

            mx = max(mx, r.val + lg + rg)
        
            return r.val + max(lg, rg)

        dfs(root)
        return mx