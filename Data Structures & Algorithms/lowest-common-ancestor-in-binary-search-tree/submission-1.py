# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs (node):
            if node is None:
                return None
            # If we find either p or q, return the current node
            if node.val == p.val or node.val == q.val:
                return node

            # Recursively search in the left and right subtrees
            left = dfs(node.left)
            right = dfs(node.right)

            # If both left and right are not None, the current node is the LCA
            if left and right:
                return node

            # Otherwise, return the non-None child (either left or right)
            return left if left else right

        ret = dfs(root)
        print (ret)
        return ret