# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        

        res = []

        def dfs(r:Optional[TreeNode], lvl:int):
            if not r:
                return
            
            if lvl == len(res):
                res.append([r.val])
            else:
                res[lvl].append(r.val)
            
            dfs(r.left, lvl + 1)
            dfs(r.right, lvl + 1)
        dfs(root, 0)

        return res
                
            
