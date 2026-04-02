# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = True  # Assume the tree is balanced initially

        def check(node):
            if not node:
                return 0  # Height of an empty tree is 0

            leftheight = check(node.left)
            rightheight = check(node.right)

            # If the difference in heights is greater than 1, mark as unbalanced
            if abs(leftheight - rightheight) > 1:
                self.res = False

            # Return the height of the current node
            return max(leftheight, rightheight) + 1

        check(root)  # Start the recursion from the root
        return self.res  # Return the final result
        