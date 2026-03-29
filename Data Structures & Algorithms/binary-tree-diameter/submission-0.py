# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        mx = 0
        def helper(r:Optional[TreeNode]):
            nonlocal mx
            lft = 1 + helper(r.left) if r.left else 0
            rght = 1 + helper(r.right) if r.right else 0
            mx = max(mx, lft + rght)
            return max(lft, rght)
        if not root:
            return 0
        helper(root)
        return mx
