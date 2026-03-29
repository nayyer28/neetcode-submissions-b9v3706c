# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def help(r:Optional[TreeNode],mx):
            out = 0
            if not r:
                return 0
            if r.val >= mx:
                mx = r.val
                out = 1
            
            out += help(r.left, mx)
            out += help(r.right, mx)
            return out
        out = help(root, float("-inf"))
        return out
            
        