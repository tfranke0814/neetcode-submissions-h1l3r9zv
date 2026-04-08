# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root

        l = root.left
        r = root.right
        
        root.right = l
        root.left = r

        if l:
            l = self.invertTree(l)
        if r:
            r = self.invertTree(r)
        

        root.right = l
        root.left = r
        return root