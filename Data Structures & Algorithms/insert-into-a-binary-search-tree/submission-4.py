# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if root is None: 
            return TreeNode (val)
        def helper (prev, node):
            if node is None: 
                if prev.val < val: 
                    prev.right = TreeNode (val)
                else: 
                    prev.left = TreeNode (val)
                return 

            if val <= node.val:
                helper (node, node.left)

            if val > node.val:
                helper (node,node.right)

            return
        helper (root, root)
        return root


