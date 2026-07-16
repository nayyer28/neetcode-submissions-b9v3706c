# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        cnt = 0
        def dfs(r: Optional[TreeNode], mx):
            nonlocal cnt
            if not r:
                return
            
            if r.val >= mx:
                mx = r.val
                cnt += 1
            
            dfs(r.left, mx)
            dfs(r.right, mx)
        
        dfs(root, float("-inf"))
        return cnt

            