# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        mx = float("-inf")

        def findGain(r:Optional[TreeNode]) -> int:
            nonlocal mx
            if not r:
                return 0 # no gain

            leftGain = max(0,findGain(r.left))
            rightGain = max(0, findGain(r.right))

            mx = max(mx, leftGain + rightGain + r.val) # negatives are neutralized so leftGain + r.val and rightGain + r.val are not needed separately

            return r.val + max(leftGain, rightGain)
        
        findGain(root)
        return mx