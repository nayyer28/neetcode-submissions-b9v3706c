# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        mx = float("-inf")
        def dfs(r:Optional[TreeNode]) -> int:
            nonlocal mx
            left = 1 + dfs(r.left) if r.left else 0
            right = 1 + dfs(r.right) if r.right else 0

            mx = max(mx, left + right)
            return max(left, right)
        
        dfs(root)
        return mx
        
        
            
        
            

            
