# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # always traverse by level ordered from right most

        res = []

        if not root:
            return res

        def traverse(r: Optional[TreeNode], lvl: int):
            nonlocal res
            if len(res) == lvl:  # lvl done
                res.append(r.val)
            if r.right:
                traverse(r.right, lvl + 1)
            if r.left:
                traverse(r.left, lvl + 1)
        traverse(root, 0)
        return res
