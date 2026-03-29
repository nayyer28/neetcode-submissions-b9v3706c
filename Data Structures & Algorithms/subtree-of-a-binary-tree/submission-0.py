# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSame(p:Optional[TreeNode], q:Optional[TreeNode]) -> bool:
            if not p and not q:
                return True

            if q and not p or p and not q:
                return False
            
            if p.val != q.val:
                return False
            
            lftSame = isSame(p.left, q.left)

            if not lftSame:
                return False
            
            rghtSame = isSame(p.right, q.right)
            
            return rghtSame
        
        if not subRoot:
            return True
        
        if not root:
            return False
        

        if isSame(root,subRoot):
            return True
        elif self.isSubtree(root.left, subRoot):
                return True
        elif self.isSubtree(root.right, subRoot):
            return True
        else:
            return False
        

                
        

            