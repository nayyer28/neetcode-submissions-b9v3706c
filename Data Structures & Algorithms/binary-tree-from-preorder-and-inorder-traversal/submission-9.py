# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        imap = {}
        for i , n in enumerate(inorder):
            imap[n] = i
        po = 0
        def dfs(l, r):
            nonlocal po
            
            if l > r:
                return None
            
            val = preorder[po]
            root = TreeNode(val=val)
            index = imap[val] # pos in inorder
            po += 1

            root.left = dfs(l, index - 1)
            root.right = dfs(index + 1, r)

            return root
        
        return dfs( 0, len(inorder) - 1 )


            


            


