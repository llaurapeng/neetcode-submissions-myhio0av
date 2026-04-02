# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.ret = True
        def dfs (node):
            if node is None: 
                return 0 

            left = dfs (node.left) + 1
            right = dfs (node.right) + 1

            if abs (left - right) > 1: 
                #whole thing is false
                self.ret = False

                
            return max (left, right)
        if dfs (root) == True: 
            return True
        else: 
            return self.ret

            
            



