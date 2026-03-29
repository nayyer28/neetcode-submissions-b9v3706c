# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:   
        res = 0
        def dfs(r: Optional[TreeNode]):
            # if we have a left, we go to that
            nonlocal res
            nonlocal k
            if r.left:
                dfs(r.left)
            k -= 1
            if k == 0:
                res = r.val
                return
            if r.right:
                dfs(r.right)
        dfs(root)
        return res
            

            
            

            





        