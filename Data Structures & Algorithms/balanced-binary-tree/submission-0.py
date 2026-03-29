# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(r: Optional[TreeNode]) -> (int,bool):
            if not r:
                return (0, True)
            
            lft_h, lft_bal = helper(r.left)
            lft_h += 1

            if not lft_bal:
                return (0,False)
            
            (rght_h, rght_bal) = helper(r.right)
            rght_h += 1
            
            if not rght_bal:
                return (0,False)
            
            return (max(lft_h,rght_h), abs(rght_h - lft_h) <= 1)
        

        return helper(root)[1]
            

            