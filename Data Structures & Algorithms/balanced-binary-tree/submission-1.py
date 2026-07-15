# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        

        def dfs(r:Optional[TreeNode])-> (bool, int):
            if not r:
                return (True, 0)
            
            leftBal, leftDep = dfs(r.left)
            if not leftBal:
                return (False, 0)

            rightBal, rightDep = dfs(r.right)
            if not rightBal:
                return (False, 0)

            if abs(leftDep - rightDep) > 1:
                return (False, 0)

            return( True, 1 + max(leftDep, rightDep) )
        
        return dfs(root)[0]

