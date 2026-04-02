# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ret = []
        
        def helper (root):

            if root is None: 
                return 0 

            helper (root.left)

            ret.append (root.val)

            helper (root.right)



        helper (root)
        print (ret)

        return ret [k-1]
