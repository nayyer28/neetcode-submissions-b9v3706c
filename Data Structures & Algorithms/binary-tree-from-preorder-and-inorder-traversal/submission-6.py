# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hmap = {}
        for i,n in enumerate(inorder):
            hmap[n] = i
        po = 0
        def dfs(l,r):
            nonlocal po
            
            if l > r:
                return None

            root = TreeNode(val=preorder[po])
            i = hmap[preorder[po]]
            po += 1
            
            root.left = dfs(l,i-1)
            root.right = dfs(i+1,r)
            return root
        
        return dfs(0,len(inorder) - 1)
