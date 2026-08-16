# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
                                                # min, max
        def dfs(r: Optional[TreeNode]) -> (bool, int, int):
            mn = mx = r.val
            if not r.left and not r.right:
                return (True, mn, mx)
            
            if r.left:
                lft_val, lft_mn, lft_mx = dfs(r.left)
                if not lft_val or r.val <= lft_mx:
                    return (False, -1, -1)
                mn = min(mn, lft_mn)
                mx = max(mx, lft_mx)
            
            if r.right:
                rght_val, rght_mn, rght_mx = dfs(r.right)
                if not rght_val or r.val >= rght_mn:
                    return (False, -1 , -1)
                mn = min(mn, rght_mn)
                mx = max(mx, rght_mx)
                
            return (True, mn, mx)

        return dfs(root)[0]
            

            

        
        return dfs(root)[0]