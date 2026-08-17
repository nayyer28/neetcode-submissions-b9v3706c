# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "N"
        
        val = f"{root.val}" # actual value as string
        size = f"{len(val)}"    # char len of value

        serial = size + "#" + val

        # pre-order : root -> left -> right
        return serial + self.serialize(root.left) + self.serialize(root.right)
        

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        print(data)
        p = 0
        def dfs() -> Optional[TreeNode]:
            nonlocal p

            if p == len(data):
                return None
            
            if data[p] == 'N':
                p += 1
                return None

            size = ''

            while data[p] != '#':
                size += data[p]
                p += 1
            
            val = int(data[p+1: p+1 + int(size)])
            p += 1 + int(size)
            
            node = TreeNode(val= int(val))

            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
            
            
            

