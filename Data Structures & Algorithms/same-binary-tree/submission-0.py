# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base Cases
        if p is None and q is None:
            return True  # Both trees are empty
        if p is None or q is None:
            return False  # One tree is empty
        if p.val != q.val:
            return False  # Mismatched values

        # Recursive Calls
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        