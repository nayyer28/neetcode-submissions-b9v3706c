# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "N"
        val = f"{root.val}"
        size = f"{len(val)}#"
        serial = size + val
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        return serial + left + right

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # 124NN5NN36NNN
        p = 0
        def dfs():
            nonlocal p
            if p == len(data):
                return None 
            if data[p] == "N":
                p += 1
                return None      
            size = ""
            while data[p] != "#":
                size += data[p]
                p += 1
            curr = data[p+1:p+1+int(size)]
            p += int(size) + 1

            r = TreeNode(val=int(curr))
            r.left = dfs()
            r.right = dfs()
            return r
        return dfs()