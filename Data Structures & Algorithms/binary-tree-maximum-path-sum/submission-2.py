# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        mx = float("-inf")

        def findMaxPath(r:Optional[TreeNode]) -> float:
            nonlocal mx
            if not r:
                return float("-inf")
            mxPathLeft = findMaxPath(r.left)
            mxPathRight = findMaxPath(r.right)
            mxPathLeftWithMe = max(mxPathLeft,0) + r.val
            mxPathRightWithMe = max(mxPathRight,0) + r.val
            maxPathLeft2Right = max(mxPathLeft,0) + max(mxPathRight,0) + r.val
            mx = max(mx, mxPathLeft, mxPathRight, mxPathLeftWithMe, mxPathRightWithMe, maxPathLeft2Right)
            return max(mxPathLeftWithMe,mxPathRightWithMe)
        findMaxPath(root)
        return mx