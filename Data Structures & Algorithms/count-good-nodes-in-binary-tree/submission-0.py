# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        out = 0
        def help(r:Optional[TreeNode],mx):
            nonlocal out
            if not r:
                return
            if r.val >= mx:
                mx = r.val
                out += 1
            
            help(r.left, mx)
            help(r.right, mx)
        help(root, float("-inf"))
        return out
            
        