# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(r: Optional[TreeNode]) -> (bool, int, int):
            if not r:
                return (True, float("-inf"), float("inf"))
            
            lft_valid, lft_mx, lft_mn = dfs(r.left)
            rght_valid, rght_mx, rght_mn = dfs(r.right)
            mx = max(r.val, rght_mx, lft_mx)
            mn = min(r.val, lft_mn, rght_mn)
            if not lft_valid or r.val <= lft_mx or not rght_valid or r.val >= rght_mn:
                return (False, mx, mn)
            return (True, mx, mn)
        isValid, _, _ = dfs(root)
        return isValid